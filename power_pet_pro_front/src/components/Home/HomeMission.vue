<template>
  <section class="hero is-halfheight heroImage">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="card card-shadow">
          <div class="card-content">
            <h2 class="title is-2 has-text-centered">Our Mission</h2>
            <hr />
            <div class="content">
             {{ mission_statement }}
            </div>
          </div>
          <footer class="card-footer">
            <a href="#" class="card-footer-item">Save</a>
            <a href="#" class="card-footer-item">Edit</a>
            <a href="#" class="card-footer-item">Delete</a>
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
      mission_statement: ''
    };
  },
  created(){
    axios.get('admin_panel/our_mission/').then(response=>{
      this.mission_statement = response.data.main_statement
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
