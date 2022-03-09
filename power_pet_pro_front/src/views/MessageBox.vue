<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Message to the Message Box</p>
        <hr />
        <p class="subtitle">
          Please Enter the follow information below to add a Message
        </p>

        <div class="columns is-centered">
          <!-- Here we are going to the box to display the messages -->
          <div class="column is-5">
            <div class="box">
              <div
                class="box"
                v-for="(message, index) in messageboxes"
                :key="index"
              >
                <span> {{ index + 1 }}. {{ message.msg }}&nbsp; </span>
                <span>
                  <button
                    class="button is-warning is-small"
                    @click="edit_message_activation(message)"
                  >
                    <span class="icon is-small">
                      <i class="fas fa-pencil-alt"></i>
                    </span>
                    <span>Edit</span></button
                  >&nbsp;
                </span>
                <span>
                  <button
                    class="button is-danger is-small"
                    @click="delete_message_activation(message)"
                  >
                    <span>Delete</span>
                    <span class="icon is-small">
                      <i class="fas fa-times"></i>
                    </span>
                  </button>
                </span>
              </div>
            </div>
          </div>

          <!-- Here we are going to the box to add messages -->
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_message()">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>

              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Message "
                    v-model="message"
                  />
                </div>
              </div>

              <div class="field" v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
              <button class="button is-success">Submit Message</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div
    class="modal is-centered"
    :class="{ 'is-active': activate_modal, 'is-clipped': activate_modal }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Edit Message</p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">Current Message: "{{ chosen_message }}"</div>
        <textarea class="textarea" v-model="chosen_message"></textarea>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-success" @click="edit_message()">
          Save changes
        </button>
        <button class="button" @click="activate_modal = false">Cancel</button>
      </footer>
    </div>
  </div>

  <div
    class="modal is-centered"
    :class="{
      'is-active': activate_delete_modal,
      'is-clipped': activate_delete_modal,
    }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm Delete Message</p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_delete_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">Current Message: "{{ chosen_message }}"</div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-danger" @click="delete_message()">
          Delete Message
        </button>
        <button class="button" @click="activate_delete_modal = false">
          Cancel
        </button>
      </footer>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { mapState } from "vuex";
import { toast } from "bulma-toast";

export default {
  name: "MessageBox",
  data() {
    return {
      message: "",
      error_message: "",
      activate_modal: false,
      chosen_message: "",
      chosen_message_id: null,
      activate_delete_modal: false,
    };
  },
  methods: {
    submit_message() {
      if (this.message) {
        // if these exists then we are going to submit the product
        axios
          .post(
            "admin_panel/message_box/post/",
            {
              msg: this.message,
            },
            { headers: { Authorization: `Bearer ${this.accessToken}` } }
          )
          .then(() => {
            this.messageboxes.push({ msg: this.message });
            this.message = "";
          })
          .catch((err) => {
            console.log(err.response.data.msg);
            this.error_message = err.response.data.msg[0];
          });
      }
    },
    edit_message_activation(msg_obj) {
      this.activate_modal = true;
      this.chosen_message = msg_obj.msg;
      this.chosen_message_id = msg_obj.id;
    },
    edit_message() {
      // Once we activate this function we want to update our message with the chosen_message
      axios
        .put(`admin_panel/message_box/update/${this.chosen_message_id}/`, {
          msg: this.chosen_message, // NOTE: this.chosen_message will be the most updated message from modal textarea
        })
        .then((response) => {
          this.activate_modal = false;
          let msg_changed = this.messageboxes.filter(
            (msg) => msg.id === this.chosen_message_id
          );
          msg_changed.msg = response.data.msg;
          console.log(msg_changed);
        });
    },
    delete_message_activation(message_object) {
      this.activate_delete_modal = !this.activate_delete_modal;
      this.chosen_message_id = message_object.id;
      this.chosen_message = message_object.msg;
    },
    delete_message() {
      axios
        .delete(`admin_panel/message_box/update/${this.chosen_message_id}/`, {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        .then((response) => {
          toast({
            message: response.data.success,
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
          this.activate_delete_modal = !this.activate_delete_modal;
        });
    },
  },
  computed: {
    ...mapState(["messageboxes", "accessToken"]),
  },
  created() {
    console.log(this.messageboxes);
  },
};
</script>
