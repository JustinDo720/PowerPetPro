<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Mission Topic</p>
        <hr />
        <p class="subtitle">Please modify or add your Mission Topic below</p>

        <div class="columns is-centered">
          <!-- Here we are going to the box to display the messages -->
          <div class="column is-5">
            <div class="box has-text-centered">
              <h1 class="title is-3">Your Current Mission Statement Topics:</h1>
              <div v-if="mission_statement_topics">
                <ul>
                  <li
                    v-for="(topic, index) in mission_statement_topics"
                    :key="index"
                  >
                    {{ index + 1 }}. {{ topic.topic }}
                    <button
                      class="button is-warning is-light is-small"
                      @click="edit_mission_topic_activation(topic)"
                    >
                      <span>Edit Topic</span>
                      <span class="icon is-small">
                        <i class="fas fa-pencil-alt"></i>
                      </span></button
                    >&nbsp;
                    <button
                      class="button is-danger is-light is-small"
                      @click="delete_mission_topic_activation(topic)"
                    >
                      <span>Delete Topic</span>
                      <span class="icon is-small">
                        <i class="fas fa-times"></i>
                      </span>
                    </button>
                  </li>
                </ul>
              </div>
              <div v-else-if="empty_topics">
                <h2 class="subtitle is-4">"{{ empty_topics }}"</h2>
              </div>
            </div>
          </div>

          <!-- Here we are going to the box to add topics -->
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
                <div class="control has-icons-left has-icons-right">
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Add a Topic"
                    v-model="new_topic"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-pen-square"></i>
                  </span>
                  <span class="icon is-small is-right">
                    <i class="fas fa-check fa-xs"></i>
                  </span>
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

  <!-- Add Mission Topic-->
  <div
    class="modal is-centered"
    :class="{ 'is-active': activate_modal, 'is-clipped': activate_modal }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Add Mission Topic</p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">New Mission Topic: "{{ new_topic }}"</div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-success" @click="submit_mission_topic()">
          Submit
        </button>
        <button class="button" @click="activate_modal = false">Cancel</button>
      </footer>
    </div>
  </div>

  <!-- Editing mission topic -->
  <div
    class="modal is-centered"
    :class="{
      'is-active': activate_edit_modal,
      'is-clipped': activate_edit_modal,
    }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Editing Mission Topic</p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_edit_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">Mission Topic: "{{ edit_topic }}"</div>
        <div class="control">
          <input class="input" type="text" v-model="edit_topic" />
        </div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-success" @click="edit_mission_topic()">
          Save Changes
        </button>
        <button class="button" @click="activate_modal = false">Cancel</button>
      </footer>
    </div>
  </div>

  <!-- Confirm deleting Mission Topic -->
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
        <p class="modal-card-title">Confirm Delete Topic</p>
        <button
          class="delete"
          aria-label="close"
          @click="activate_delete_modal = false"
        ></button>
      </header>
      <section class="modal-card-body">
        <div class="box">Current Mission Topic: "{{ delete_topic }}"</div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-danger" @click="delete_mission_topic">
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
      mission_statement_topics: [],
      new_topic: "",
      empty_topics: "",
      error_message: "",
      activate_modal: false,
      activate_delete_modal: false,
      activate_edit_modal: false,
      edit_topic_slug: null,
      edit_topic: "",
      delete_topic_slug: null,
      delete_topic: "",
    };
  },
  computed: {
    ...mapState(["accessToken"]),
  },
  methods: {
    submit_mission_topic() {
      if (this.new_topic) {
        // We did get a message from telling us that there is no mission statement which is why we are going to post
        axios
          .post(
            "admin_panel/our_mission/add_topic/",
            {
              topic: this.new_topic,
            },
            {
              headers: { Authorization: `Bearer ${this.accessToken}` },
            }
          )
          .then(() => {
            this.activate_modal = !this.activate_modal;
            toast({
              message:
                "Submitted the new mission topic. Please refresh your page.",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 6000, // milliseconds
              position: "bottom-right",
            });
          });
      } else {
        this.error_message = "Please type something in the box above.";
      }
    },
    delete_mission_topic_activation(topic) {
      this.activate_delete_modal = !this.activate_delete_modal;
      this.delete_topic_slug = topic.slug;
      this.delete_topic = topic.topic;
    },
    delete_mission_topic() {
      axios
        .delete(
          `admin_panel/our_mission/update_topic/${this.delete_topic_slug}/`,
          {
            headers: { Authorization: `Bearer ${this.accessToken}` },
          }
        )
        .then((response) => {
          console.log(response.data.message);
          this.activate_delete_modal = !this.activate_delete_modal;
          toast({
            message: "Removed your topic. Please refresh your page.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
        });
    },
    edit_mission_topic_activation(topic) {
      this.activate_edit_modal = !this.activate_edit_modal;
      this.edit_topic_slug = topic.slug;
      this.edit_topic = topic.topic;
    },
    edit_mission_topic() {
      console.log(this.edit_topic);
      axios
        .put(
          `admin_panel/our_mission/update_topic/${this.edit_topic_slug}/`,
          {
            topic: this.edit_topic,
          },
          {
            headers: { Authorization: `Bearer ${this.accessToken}` },
          }
        )
        .then(() => {
          this.activate_edit_modal = !this.activate_edit_modal;
          toast({
            message: "Updated your mission topic. Please refresh your page.",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
        });
    },
  },
  created() {
    axios.get("admin_panel/our_mission/all_topics/").then((response) => {
      if (response.data.length >= 1) {
        this.mission_statement_topics = response.data;
      } else {
        this.empty_topics = "No topics have been added";
      }
    });
  },
};
</script>
