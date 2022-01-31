<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Mission Statement</p>
        <hr />
        <p class="subtitle">
          Please modify or add your Mission Statement below
        </p>

        <div class="columns is-centered">
          <!-- Here we are going to the box to display the messages -->
          <div class="column is-5">
            <div class="box has-text-centered">
              <h1 class="title is-3">Your Current Mission Statement:</h1>
              <div v-if="mission_statement">
                <h2 class="subtitle is-4">"{{ mission_statement }}"</h2>
                <button
                  class="button is-danger is-outlined"
                  @click="activate_delete_modal = !activate_delete_modal"
                >
                  <span>Delete Mission Statement</span>
                  <span class="icon is-small">
                    <i class="fas fa-times"></i>
                  </span>
                </button>
              </div>
              <div v-else-if="empty_mission_statement">
                <h2 class="subtitle is-4">"{{ empty_mission_statement }}"</h2>
              </div>
            </div>
          </div>

          <!-- Here we are going to the box to add messages -->
          <div class="column is-5">
            <form
              class="box"
              @submit.prevent="activate_modal = !activate_modal"
            >
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>

              <div class="field">
                <div class="control has-icons-left">
                  <textarea
                    class="textarea"
                    placeholder="Mission Statement"
                    v-model="mission_statement"
                  ></textarea>
                </div>
              </div>

              <div class="field" v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
              <button class="button is-success">
                Submit Mission Statement
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Confirm Update/Post mission statement-->
  <div
    class="modal is-centered"
    :class="{ 'is-active': activate_modal, 'is-clipped': activate_modal }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">
          Confirm Posting or Updating Mission Statement
        </p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">New Mission Statement: "{{ mission_statement }}"</div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button
          class="button is-success"
          @click="confirm_submit_mission_statement()"
        >
          Save Changes
        </button>
        <button class="button" @click="activate_modal = false">Cancel</button>
      </footer>
    </div>
  </div>

  <!-- Confirm deleting Mission Statement -->
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
        <div class="box">
          Current Mission Statement: "{{ mission_statement }}"
        </div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button
          class="button is-danger"
          @click="confirm_delete_mission_statement()"
        >
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
  name: "MissionStatementBox",
  data() {
    return {
      mission_statement: "",
      empty_mission_statement: "",
      error_message: "",
      activate_modal: false,
      activate_delete_modal: false,
    };
  },
  computed: {
    ...mapState(["accessToken"]),
  },
  methods: {
    confirm_submit_mission_statement() {
      if (this.mission_statement) {
        // Now we need to see if we should post this new mission statement or update the old one
        if (this.empty_mission_statement) {
          // We did get a message from telling us that there is no mission statement which is why we are going to post
          axios
            .post(
              "admin_panel/our_mission/add_mission_statement/",
              {
                main_statement: this.mission_statement,
              },
              {
                headers: { Authorization: `Bearer ${this.accessToken}` },
              }
            )
            .then(() => {
              this.activate_modal = !this.activate_modal;
              toast({
                message:
                  "Submitted the mission statement. Please refresh your page.",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 6000, // milliseconds
                position: "bottom-right",
              });
            });
        } else {
          // Here that means we already have a mission statement which means we are just going to update it
          axios
            .put(
              "admin_panel/our_mission/add_mission_statement/",
              {
                main_statement: this.mission_statement,
              },
              {
                headers: { Authorization: `Bearer ${this.accessToken}` },
              }
            )
            .then(() => {
              this.activate_modal = !this.activate_modal;
              toast({
                message:
                  "Updated the mission statement. Please refresh your page.",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 6000, // milliseconds
                position: "bottom-right",
              });
            });
        }
      } else {
        this.error_message = "Please type something in the box above.";
      }
    },
    confirm_delete_mission_statement() {
      axios
        .delete("admin_panel/our_mission/add_mission_statement/", {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        .then(() => {
          this.activate_delete_modal = !this.activate_delete_modal;
          toast({
            message: "Deleted Mission Statement. Please refresh your page.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
        });
    },
  },
  created() {
    axios.get("admin_panel/our_mission/").then((response) => {
      if (!response.data.message) {
        this.mission_statement = response.data.main_statement;
      } else {
        this.empty_mission_statement = response.data.message;
      }
    });
  },
};
</script>
