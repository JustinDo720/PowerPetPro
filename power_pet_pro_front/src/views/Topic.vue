<template>
  <section class="hero is-fullheight is-info">
    <div class="hero-body" v-if="main_topic">
      <div class="container has-text-centered is-centered">
        <p class="title is-1">
          {{ main_topic }}
        </p>
        <hr />

        <div class="columns is-centered">
          <div class="column is-5">
            <div v-if="all_topic_details">
              <div class="box" v-for="(topic_detail, index) in all_topic_details" :key="index" >
                <h1 class="subtitle is-3 has-text-black">
                  {{ topic_detail.mission_topic_details }}
                </h1>
              </div>
            </div>
            <div v-if="empty_message">
              <div class="box">
                <h1 class="subtitle is-3 has-text-black">
                  {{ empty_message }}
                </h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default{
  name: "Topic",
  data(){
    return{
      all_topic_details: [],
      main_topic: '',
      empty_message: '',
    }
  },
  created(){
    // We need to grab the slug from the url
    let topic_slug = this.$route.params.topic_slug
    // Careful we are going to get an array of details
    axios.get(`admin_panel/our_mission/view_topic/${topic_slug}/`).then(response=>{
      console.log(response.data)
      if(response.data.length >= 1){
        this.all_topic_details = response.data
        this.main_topic = response.data[0].mission_topic_name
      } else {
        this.main_topic = response.data.topic
        this.empty_message = response.data.message
      }
    })
  }

}
</script>