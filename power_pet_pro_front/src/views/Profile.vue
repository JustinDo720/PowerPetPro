<template>
  <!-- Introduction section -->
  <section class="section is-small" v-if="user_profile">
    <div class="container has-text-centered">
      <div class="box" v-if="!isAdmin">
        <h1 class="title is-1">Hello {{ user_profile.username }}.</h1>
        <h2 class="subtitle">
          Welcome to your account page! Here, you can view or change details
          such as your phone number or address for us to make a seamless
          shipping and billing process. Please make sure the details below are
          up-to-date.
        </h2>
        <button class="button is-outlined is-primary" v-if="user_profile.feedback" @click="showFeedback=!showFeedback">
            <span>View Your Feedback</span>
        </button>
      </div>
      <div class="box" v-else>
        <h1 class="title is-1">Hello Admin {{ user_profile.username }}.</h1>
        <h2 class="subtitle">
          Welcome to your admin account page! You could access Admin tools and also view feedbacks along with seeing
          your own profile.
        </h2>
        <div>
          <button class="button is-outlined is-primary" v-if="user_profile.feedback" @click="showFeedback=!showFeedback">
            <span>View Your Feedback</span>
          </button>
        </div>
        <br>
        <div class="field has-text-centered">
          <input
            id="adminSwitch"
            type="checkbox"
            name="adminSwitch"
            class="switch is-medium is-outlined is-danger"
            checked="checked"
            v-model="admin_mode"
          />
          <label for="adminSwitch">Admin Mode</label>
        </div>
      </div>
    </div>
  </section>
  <!-- Admin section -->
  <section class="section is-small" v-if="admin_mode">
    <div class="container">
      <div class="columns is-centered">
        <div class="column">
          <div class="box">
            <h1 class="title is-1 has-text-centered">Admin Functionality</h1>
            <div class="columns is-multiline">
              <div class="column is-4" id="message-control">
                <h4 class="title is-4">Message Control</h4>
                <ul>
                  <li>
                    <router-link
                      :to="{
                        name: 'ViewAllMessages',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        View All Messages
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'MessageBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                      Add/Edit Message of the Day
                      </button>
                    </router-link>
                  </li>
                </ul>
              </div>
              <div class="column is-4" id="product-control">
                <h4 class="title is-4">Product Control</h4>
                <ul>
                  <li>
                    <router-link
                      :to="{
                        name: 'ViewAllProducts',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        View All Products
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'AdminProduct',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Product
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'AdminCategory',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Category
                      </button>
                    </router-link>
                  </li>
                </ul>
              </div>
              <div class="column is-4" id="mission-control">
                <h4 class="title is-4">Mission Control</h4>
                <ul>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionStatementBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Mission Statement
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionStatementTopicBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Mission Statement Topic
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionDetailsBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Mission Details
                      </button>
                    </router-link>
                  </li>
                </ul>
              </div>
              <div class="column is-4" id="feedback-control">
                <h4 class="title is-4">Feedback Control</h4>
                <ul>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionStatementBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add/View Questions
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionStatementTopicBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Mission Statement Topic
                      </button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'MissionDetailsBox',
                      }"
                    >
                      <button class="button is-primary is-outlined">
                        Add Mission Details
                      </button>
                    </router-link>
                  </li>
                </ul>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Information section -->
  <section class="section is-small" v-if="!edit_mode && !admin_mode">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-7">
          <div class="field has-text-centered">
            <input
              id="switchOutlinedWarning"
              type="checkbox"
              name="switchOutlinedWarning"
              class="switch is-medium is-outlined is-warning"
              v-model="edit_mode"
            />
            <label for="switchOutlinedWarning">Edit Mode</label>
          </div>
          <div
            class="card p-0"
            v-for="(user_info, index) in user_profile"
            :key="index"
          >
            <div class="card-content">
              <div class="content is-large">
                {{ cleanIndex(index) }}: {{ user_info }}
              </div>
            </div>
          </div>
        </div>
        <div class="column is-7">
          <div class="box">
            <h1 class="title is-1 has-text-centered">Recent Orders</h1>
            <OrderBox
              v-for="(order, index) in orders"
              :key="index"
              :order="order"
            ></OrderBox>
            <br />
            <router-link :to="`/profile/${user_id}/orders/`">
              <p class="has-text-centered has-text-link">View all orders</p>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Edit Information section -->
  <section class="section is-small" v-if="edit_mode && !admin_mode">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-7">
          <div class="field has-text-centered">
            <input
              id="switchEditMode"
              type="checkbox"
              name="switchEditMode"
              class="switch is-medium is-outlined is-warning"
              v-model="edit_mode"
            />
            <label for="switchEditMode">Edit Mode</label>
          </div>
          <div
            class="card p-0"
            v-for="(user_info, index) in user_profile"
            :key="index"
          >
            <div class="card-content control">
              <div class="content is-large">
                <strong>{{ cleanIndex(index) }}</strong
                >:
                <div
                  class="control has-icons-left"
                  v-if="index === 'country' || index === 'state'"
                >
                  <div class="select is-large">
                    <select
                      v-model="user_profile['country']"
                      v-if="index === 'country'"
                    >
                      <option
                        v-for="(country, index) in countries"
                        :key="index"
                      >
                        {{ country }}
                      </option>
                    </select>
                    <select
                      v-model="user_profile['state']"
                      v-else
                      @input="fetched_state"
                    >
                      <option
                        v-for="(state, index) in country_states.states"
                        :key="index"
                      >
                        {{ state }}
                      </option>
                    </select>
                    <span class="icon is-medium is-left">
                      <i class="fas fa-globe"></i>
                    </span>
                  </div>
                  &nbsp;
                  <button
                    class="button is-danger is-outlined"
                    v-if="index === 'country'"
                    @click="user_profile['country'] = ''"
                  >
                    <span>Clear Country</span>
                  </button>
                  <button
                    class="button is-danger is-outlined"
                    v-else
                    @click="user_profile['state'] = ''"
                  >
                    <span>Clear State</span>
                  </button>
                  <div>
                    <p class="is-info help">
                      * Did you know that you could click on the dropdown menu
                      and start typing to search for your Country or State *
                    </p>
                  </div>
                </div>

                <div v-if="index !== 'country' && index !== 'state'">
                  <input
                    class="input is-medium"
                    type="text"
                    v-model="user_profile[index]"
                    :disabled="
                      index === 'date_joined' ||
                      index === 'email' ||
                      index === 'username'
                    "
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="field has-text-centered">
            <p v-if="error_message" class="help is-danger">
              {{ error_message }}
            </p>
            <button
              class="button mt-3 is-primary is-light"
              v-on:click="submitEdits"
            >
              Save Changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Confirm Modal section -->
  <div class="modal" :class="{ 'is-active': showConfirm }" v-if="user_profile">
    <div class="modal-background"></div>
    <div class="modal-content">
      <!-- Any other Bulma elements you want -->
      <article class="message">
        <div class="message-header">
          <p class="has-text-centered">Confirm Information</p>
        </div>
        <div class="message-body">
          <div class="columns">
            <div class="column">
              <p v-for="(user_info, index) in user_profile" :key="index">
                <strong>{{ cleanIndex(index) }}</strong
                >: {{ user_info }}
              </p>
            </div>
            <div class="is-divider-vertical" data-content="CHANGED"></div>
            <div class="column">
              <p v-for="(user_info, index) in changed_info" :key="index">
                <strong>{{ cleanIndex(index) }}</strong
                >: {{ user_info.old_value }} <i class="fas fa-arrow-right"></i>
                {{ user_info.new_value }}
              </p>
            </div>
          </div>
          <div class="buttons has-addons is-centered">
            <button
              class="button is-danger is-light"
              @click="showConfirm = !showConfirm"
            >
              Cancel</button
            >&nbsp;
            <button class="button is-success is-light" @click="confirmEdits()">
              Confirm Changes
            </button>
          </div>
        </div>
      </article>
    </div>
    <button
      class="modal-close is-large"
      aria-label="close"
      @click="showConfirm = !showConfirm"
    ></button>
  </div>

  <!-- Feedback Modal -->
  <div class="modal" :class="{'is-active': showFeedback}" v-if="user_profile.feedback">
    <div class="modal-background"></div>
    <div class="modal-content">
      <!-- Any other Bulma elements you want -->
      <div class="card">
        <div class="card-content">
          <header class="card-header">
            <p class="card-header-title" v-if="user_profile.first_name">
              Thank you for your feedback {{ user_profile.first_name }}!
            </p>
            <p class="card-header-title" v-else>
              Thank you for your feedback {{ user_profile.username }}!
            </p>
          </header>
          <div class="content">
            <strong>Opinions:</strong> "{{ user_profile.feedback.opinions }}"
          </div>
          <div class="content">
            <strong>Suggestion:</strong> "{{ user_profile.feedback.suggestions }}"
          </div>
          <div class="content">
              <strong>
                Q&A
              </strong>
             <div v-for="(a,q, index) in user_profile.feedback.answers" :key="index">
              <strong>{{q}}</strong>: {{ a }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <button class="modal-close is-large" aria-label="close" @click="showFeedback=!showFeedback"></button>
  </div>
</template>
<script>
import axios from "axios";
import Cookies from "cookies-js";
import { toast } from "bulma-toast";
import countries from "../assets/Profile/countries";
import countries_and_states from "../assets/Profile/countries_and_states";
import OrderBox from "../components/OrderBox";
// import { mapGetters } from "vuex"

export default {
  name: "Profile",
  data() {
    return {
      // Careful with setting things null they might show "Null error" so just change it to string format
      // user_profile: null,
      user_profile: '', // This is where we are going to store all of our user Profile details
      original_profile: '', // We are going to use this to check if they user changed anything
      countries: [],
      states: '',
      edit_mode: false,
      admin_mode: true,
      showConfirm: false,
      showFeedback: false,
      isAdmin: false,
      error_message: "",
      changed_info: "",
      orders: [],
    };
  },
  components: {
    OrderBox,
  },
  methods: {
    cleanIndex(index) {
      const clean_words = index.split("_");
      for (let i = 0; i < clean_words.length; i++) {
        // We want to capitalize each letter and add that on to everything else but the first letter
        clean_words[i] =
          clean_words[i][0].toUpperCase() + clean_words[i].substr(1); // substr is like slicing in py [1:]
      }
      return clean_words.join(" ");
    },
    submitEdits() {
      let changed_user_info = {};
      // We are going to find which fields they changed
      for (let user_profile_key in this.user_profile) {
        let new_value = this.user_profile[user_profile_key];
        let old_value = this.original_profile[user_profile_key];
        // Make sure you check for new_value being null because if it is then we cant compare
        if (new_value !== null && new_value !== old_value) {
          changed_user_info[user_profile_key] = {
            old_value: old_value,
            new_value: new_value,
          };
        }
      }

      // if changed_user_info has an obj that means they did change something
      if (Object.keys(changed_user_info).length > 0) {
        this.changed_info = changed_user_info;
        this.showConfirm = !this.showConfirm;
      } else {
        this.error_message =
          "Your info hasn't changed. Please make an edit then save changes.";
      }
    },
    confirmEdits() {
      let changed_data = {
        user: this.user_id,
      };
      let config = {
        headers: { Authorization: `Bearer ${this.accessToken}` },
      };
      for (let key in this.changed_info) {
        changed_data[key] = this.changed_info[key].new_value;
      }
      console.log(changed_data);
      axios
        .put(`profile_list/user_profile/${this.user_id}/`, changed_data, config)
        .then((response) => {
          this.showConfirm = !this.showConfirm;
          this.edit_mode = !this.edit_mode;
          toast({
            message: "Your Account Page has been updated",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 30000, // milliseconds
            position: "bottom-right",
          });
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
  computed: {
    user_id() {
      return Cookies("user_id");
    },
    accessToken() {
      return Cookies("accessToken");
    },
    country_states() {
      let country_selected = {};
      if (this.user_profile["country"]) {
        let state_obj = this.states.filter(
          (country) => country.country === this.user_profile["country"]
        );
        country_selected = state_obj[0]; // the thing is we are getting an array back so we need to grab the first result
      } else {
        country_selected = { states: ["Please choose a country first!!"] }; // We need this to make sure that country_states return something not null
      }
      return country_selected;
    },
  },
  created() {

    // We are going to set our model countries to the our country objects
    this.states = countries_and_states.countries;
    this.states.forEach((country) => {
      this.countries.push(country.country);
    });
    // we are going to use our cookies because mounted() runs up before our store
    axios
      .get(`profile_list/user_profile/${this.user_id}/`, {
        headers: { Authorization: `Bearer ${this.accessToken}` },
      })
      .then((response) => {
        this.user_profile = response.data;
        this.isAdmin = response.data.is_staff;
        if(!this.isAdmin){
          this.admin_mode = false
        }
        // Once we set isAdmin we don't need is_staff to display on profile
        delete response.data.is_staff
        let original_data = {};
        for (let key in response.data) {
          original_data[key] = response.data[key];
        }
        this.original_profile = original_data;
      });
    axios
      .get(`latest_orders/${this.user_id}/`, {
        headers: { Authorization: `Bearer ${this.accessToken}` },
      })
      .then((response) => {
        this.orders = response.data;
      });
  },
};
</script>
