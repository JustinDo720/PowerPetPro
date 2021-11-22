<template>
  <section class="hero is-halfheight heroImage">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="card card-shadow">
          <div class="card-content">
            <h2 class="title is-2 has-text-centered">Our Mission</h2>
            <hr />
            <div class="content" v-if="!blank_statement">
             {{ mission_statement }}
            </div>
            <div class="content" v-else>
             {{ blank_statement }}
            </div>
          </div>
          <footer class="card-footer">
            <router-link :to="{name:'Topic', params:{topic_slug: topic.slug }}"
                         v-for="(topic, index) in topics" :key="index"
                         class="card-footer-item">
                {{ topic.topic }}
            </router-link>
            <p class="card-footer-item has-text-centered" v-if="blank_topic">
              {{ blank_topic }}
            </p>
          </footer>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeMission",
  data() {
    return {
      mission_statement: '',
      blank_statement: '',  // Error Message for no Mission Statement
      topics: [],
      blank_topic: '',  // Error Message for no Topic
    };
  },
  created(){
    axios.get('admin_panel/our_mission/').then(response=>{
      this.mission_statement = response.data.main_statement
    }).catch(()=>{
      this.blank_statement = 'Currently, there are no mission statement. Please login to your admin account to add one.'
    })
    axios.get('admin_panel/our_mission/all_topics/').then(response=>{
      this.topics = response.data
    }).catch(()=>{
      this.blank_topic = 'Currently, there are no topics. Please login to your admin account to add one.'
    })
  }
};
</script>

<style scoped>
.heroImage {
  background-image: url("../../assets/dog_friend.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
