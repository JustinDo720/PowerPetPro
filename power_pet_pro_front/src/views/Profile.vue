<template>
  <!-- Introduction section -->
  <section class="section is-small" v-if="user_profile">
    <div class="container has-text-centered">
      <div class="box">
        <h1 class="title is-1">
          Hello {{ user_profile.username }}.
        </h1>
        <h2 class="subtitle">
          Welcome to your account page! Here, you can view or change details such as your phone number or address
          for us to make a seamless shipping and billing process. Please make sure the details below are up-to-date.
        </h2>
      </div>
    </div>
  </section>
  <!-- Information section -->
   <section class="section is-small" v-if="!edit_mode">
     <div class="container">
       <div class="columns is-centered">
         <div class="column is-7">
             <div class="field has-text-centered">
              <input id="switchOutlinedWarning"
                     type="checkbox" name="switchOutlinedWarning" class="switch is-medium is-outlined is-warning"
                     v-model="edit_mode">
              <label for="switchOutlinedWarning">Edit Mode</label>
            </div>
            <div class="card p-0" v-for="(user_info, index) in user_profile" :key="index">
              <div class="card-content">
                <div class="content is-large">
                  {{ cleanIndex(index)  }}: {{ user_info }}
                </div>
              </div>
            </div>
         </div>
       </div>
     </div>
  </section>
  <!-- Edit Information section -->
  <section class="section is-small" v-else>
   <div class="container">
     <div class="columns is-centered">
       <div class="column is-7">
           <div class="field has-text-centered">
            <input id="switchEditMode"
                   type="checkbox" name="switchEditMode" class="switch is-medium is-outlined is-warning"
                   v-model="edit_mode">
            <label for="switchEditMode">Edit Mode</label>
          </div>
          <div class="card p-0" v-for="(user_info, index) in user_profile" :key="index">
            <div class="card-content control">
              <div class="content is-large">
                <strong>{{ cleanIndex(index)  }}</strong>:
                <div class="control has-icons-left"  v-if="index === 'country' || index === 'state' ">
                  <div class="select is-large">
                    <select v-model="user_profile['country']" v-if="index === 'country'">
                      <option v-for="(country,index) in countries" :key="index">
                        {{ country }}
                      </option>
                    </select>
                    <select v-model="user_profile['state']" v-else @input="fetched_state">
                      <option v-for="(state,index) in country_states.states" :key="index">
                        {{ state }}
                      </option>
                    </select>
                    <span class="icon is-medium is-left">
                      <i class="fas fa-globe"></i>
                    </span>
                  </div>&nbsp;
                  <button class="button is-danger is-outlined" v-if="index === 'country'"
                          @click="user_profile['country'] = ''">
                      <span>Clear Country</span>
                  </button>
                   <button class="button is-danger is-outlined" v-else
                            @click="user_profile['state'] = ''">
                      <span>Clear State</span>
                  </button>
                      <div>
                  <p class="is-info help">
                    * Did you know that you could click on the dropdown menu and start typing to search for your Country or State *
                  </p>
                </div>
                </div>


                <div v-if="index !== 'country' && index !== 'state' ">
                  <input class="input is-medium" type="text" v-model="user_profile[index]"
                     :disabled="index === 'date_joined' || index === 'email' || index === 'username'"
                     >
                </div>

              </div>
            </div>
          </div>
         <div class="field has-text-centered">
           <p v-if="error_message" class="help is-danger">
             {{ error_message }}
           </p>
           <button class="button mt-3 is-primary is-light" v-on:click="submitEdits">Save Changes</button>
         </div>
         </div>
       </div>
     </div>
  </section>

  <!-- Confirm Modal section -->
  <div class="modal" :class="{'is-active':showConfirm}">
    <div class="modal-background"></div>
    <div class="modal-content">
      <!-- Any other Bulma elements you want -->
      <article class="message">
        <div class="message-header">
          <p class="has-text-centered">
            Confirm Information
          </p>
        </div>
        <div class="message-body">
          <div class="columns">
            <div class="column">
              <p v-for="(user_info, index) in user_profile" :key="index">
                <strong>{{ cleanIndex(index) }}</strong>: {{ user_info }}
              </p>
            </div>
            <div class="is-divider-vertical" data-content="CHANGED"></div>
            <div class="column">
              <p v-for="(user_info, index) in changed_info" :key="index">
                <strong>{{ cleanIndex(index) }}</strong>: {{ user_info.old_value }}
                <i class="fas fa-arrow-right"></i> {{ user_info.new_value }}
              </p>
            </div>
          </div>
          <div class="buttons has-addons is-centered">
            <button class="button is-danger is-light" @click="showConfirm = !showConfirm">Cancel</button>&nbsp;
            <button class="button is-success is-light" @click="confirmEdits()">Confirm Changes</button>
          </div>
        </div>

      </article>
    </div>
    <button class="modal-close is-large" aria-label="close" @click="showConfirm = !showConfirm"></button>
  </div>
</template>
<script>
import axios from 'axios'
import Cookies from 'cookies-js'
import { toast } from 'bulma-toast'
import countries from "../assets/Profile/countries";
import countries_and_states from '../assets/Profile/countries_and_states'

export default{
  name: "Profile",
  data(){
    return {
      user_profile: null, // This is where we are going to store all of our user Profile details
      original_profile: null, // We are going to use this to check if they user changed anything
      countries: [],
      states: null,
      edit_mode: false,
      showConfirm: false,
      error_message: '',
      changed_info: '',
    }
  },
  methods: {
    cleanIndex(index){
      const clean_words = index.split("_")
      for(let i = 0; i < clean_words.length; i++){
        // We want to capitalize each letter and add that on to everything else but the first letter
        clean_words[i] = clean_words[i][0].toUpperCase() + clean_words[i].substr(1) // substr is like slicing in py [1:]
      }
      return clean_words.join(" ")
    },
    submitEdits(){
      let changed_user_info = {}
      // We are going to find which fields they changed
      for(let user_profile_key in this.user_profile){
        let new_value = this.user_profile[user_profile_key]
        let old_value = this.original_profile[user_profile_key]
        // Make sure you check for new_value being null because if it is then we cant compare
        if(new_value !== null && new_value !== old_value){
           changed_user_info[user_profile_key] = {
                'old_value': old_value,
                'new_value': new_value
              }
        }
      }

      // if changed_user_info has an obj that means they did change something
      if(Object.keys(changed_user_info).length > 0){
        this.changed_info = changed_user_info
        this.showConfirm = !this.showConfirm
      }else{
        this.error_message = "Your info hasn't changed. Please make an edit then save changes."
      }
    },
    confirmEdits(){
      let changed_data = {
        user: this.user_id
      }
      let config = {
        headers: { Authorization: `Bearer ${this.accessToken}` }
      }
      for(let key in this.changed_info){
        changed_data[key] = this.changed_info[key].new_value
      }
      console.log(changed_data)
      axios.put(`profile_list/user_profile/${this.user_id}/`, changed_data, config).then(response=>{
        console.log(response.data)
        this.showConfirm = !this.showConfirm
        this.edit_mode = !this.edit_mode
         toast({
            message: 'Your Account Page has been updated',
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 30000, // milliseconds
            position: "bottom-right",
          });
      }).catch(err=>{
        console.log(err.response)
      })
    }
  },
  computed:{
    user_id(){
      return  Cookies('user_id')
    },
    accessToken(){
      return  Cookies('accessToken')
    },
    country_states(){
      let country_selected = {}
      if(this.user_profile['country']){
        let state_obj = this.states.filter(country => country.country === this.user_profile['country'])
        country_selected = state_obj[0] // the thing is we are getting an array back so we need to grab the first result
      }else{
        country_selected = {states: ['Please choose a country first!!']} // We need this to make sure that country_states return something not null
      }
      console.log(country_selected)
      return country_selected
    }
  },
  created(){
    // We are going to set our model countries to the our country objects
    this.states = countries_and_states.countries
    this.states.forEach(country => {
      this.countries.push(country.country)
    })
    console.log(this.countries)
    // we are going to use our cookies because mounted() runs up before our store
    axios.get(`profile_list/user_profile/${this.user_id}/`,{
       headers: { Authorization: `Bearer ${this.accessToken}` }
    }).then(response=>{
      this.user_profile = response.data
      let original_data = {}
      for(let key in response.data){
        original_data[key] = response.data[key]
      }
      this.original_profile = original_data
    })
  }
}
</script>