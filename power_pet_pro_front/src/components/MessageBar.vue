<template>
  <div class="container is-fluid messageBackground">
        <nav class="pagination is-centered" role="navigation" aria-label="pagination">
          <button class="button is-ghost is-large pagination-previous" @click="changeMessage(previous)">
            <span class="icon is-medium">
              <i class="fas fa-long-arrow-alt-left"></i>
            </span>

          </button>
          <button class="button is-ghost is-large pagination-next" @click="changeMessage(next)">
            <span class="icon is-medium">
              <i class="fas fa-long-arrow-alt-right"></i>
            </span>
          </button>
          <ul class="pagination-list">
            <li>
              <p v-for="(message, index) in message_bar" :key="index" class="whiteText">
                {{ message.msg }}
              </p>
            </li>
          </ul>
        </nav>
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
  data(){
    return{
      message_bar: [],
      next: '',
      previous: '',
    }
  },
  methods:{
    changeMessage(url){
      if(url !== null){
         axios.get(url).then(response=>{
           this.message_bar = response.data.results
           this.next = response.data.next
           this.previous = response.data.previous
      })
      }
    }
  },
  beforeMount() {
    // run one for message bar
    axios.get('admin_panel/message_bar/').then(response=>{
      this.message_bar = response.data.results
      this.next = response.data.next
      this.previous = response.data.previous
    })
  },
  created(){
      // now we need to get all the messages to put them into state.messageboxes
    axios.get('admin_panel/message_box/').then(response=>{
      this.$store.commit('fetch_message_box', {
        messages:response.data.results,
        next: response.data.next,
        previous: response.data.previous
      })
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
