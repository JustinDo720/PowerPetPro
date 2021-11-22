<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding Details to a Topic</p>
        <hr />
        <p class="subtitle">Please Enter the follow information below to add a Detail</p>
        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_details()">
              <div class="field">
                  <h1 class="title is-4">Topic: </h1>
                  <div class="select is-medium">
                    <select v-model="chosen_topic">
                      <option v-for="(topic, index) in all_topics" :key="index" >
                        {{ topic.topic }}
                      </option>
                    </select>
                  </div>
              </div>
              <div class="field">
                <div class="control">
                  <textarea class="textarea is-primary" placeholder="Topic Description"
                            v-model="topic_details" rows="8"></textarea>
                </div>
              </div>
              <button class="button is-success is-outlined">Submit Topic Description</button>
              <p class="help is-danger" v-if="error_message">
                {{ error_message }}
              </p>

            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { mapState } from 'vuex';
import {toast} from "bulma-toast";

export default{
  name: 'MissionDetailsBox',
  data(){
    return{
      chosen_topic: '',
      topic_details: '',
      all_topics: [],
      error_message: '',
      process_error: '',
    }
  },
  methods:{
    submit_details(){
      if(this.chosen_topic && this.topic_details){
         let topic_object = this.all_topics.find(topic => topic.topic === this.chosen_topic)
         axios.post('admin_panel/our_mission/add_details/',{
            mission_topic: topic_object.id,
            mission_topic_details: this.topic_details,
         }, {
           headers : {Authorization: `Bearer ${this.accessToken}` }
         }).then(()=>{
           toast({
            message: `Mission Detail has been added to product list`,
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
         }).catch((err)=>{
           this.error_message = 'Your characters are more than 800 characters'
         })
      }else{
        this.error_message = 'Please fill out both areas before submitting.'
      }
    }
  },
  computed:{
    ...mapState(['accessToken'])
  },
  created(){
    axios.get('admin_panel/our_mission/all_topics/').then((response)=>{
      this.all_topics = response.data
    })
  }

}
</script>