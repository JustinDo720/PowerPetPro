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
                <strong>{{ cleanIndex(index)  }}</strong>: <input class="input is-medium" type="text" :placeholder="user_info">
              </div>
            </div>
          </div>
         <div class="field has-text-centered">
           <button class="button mt-3 is-primary is-light" v-on:click="showConfirm = !showConfirm">Save Changes</button>
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
          <p v-for="(user_info, index) in user_profile" :key="index">
            <strong>{{ cleanIndex(index) }}</strong>: {{ user_info }}
          </p>
          <div class="buttons has-addons is-centered">
            <button class="button is-danger is-light" @click="showConfirm = !showConfirm">Cancel</button>&nbsp;
            <button class="button is-success is-light" @click="submitEdits">Confirm Changes</button>
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

export default{
  name: "Profile",
  data(){
    return {
      user_profile: null, // This is where we are going to store all of our user Profile details
      edit_mode: false,
      showConfirm: false,

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
      console.log('Confirming')
    }
  },
  computed:{

  },
  created(){
    const user_id = Cookies('user_id')
    const  accessToken = Cookies('accessToken')
    // we are going to use our cookies because mounted() runs up before our store
    axios.get(`profile_list/user_profile/${user_id}/`,{
       headers: { Authorization: `Bearer ${accessToken}` }
    }).then(response=>{
      this.user_profile = response.data
    })
  }
}
</script>