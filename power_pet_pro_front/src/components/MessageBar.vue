<template>
  <div class="container is-fluid messageBackground">
    <div>
      <p v-for="(message, index) in messageboxes" :key="index" class="whiteText">
        {{ message.msg }}
      </p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from "axios";

export default {
  name: "MessageBar",
  computed:{
    ...mapState(['messageboxes'])
  },
  created(){
      // now we need to get all the messages to put them into state.messageboxes
    axios.get('admin_panel/message_box/').then(response=>{
      this.$store.commit('fetch_message_box', {messages:response.data.results})
    })
  }
};

</script>

<style scoped>
.messageBackground {
  background-color: black;
  justify-content: center;
  display: flex;
}
.whiteText {
  color: white;
}
</style>
