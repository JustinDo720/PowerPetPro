<template>
  <section class="hero is-fullheight ">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Message to the Message Box</p>
        <hr />
        <p class="subtitle">Please Enter the follow information below to add a Message</p>

        <div class="columns is-centered">

          <!-- Here we are going to the box to display the messages -->
           <div class="column is-5">
             <div class="box">
                 <div class="box" v-for="(message, index) in messageboxes" :key="index">
                  {{index + 1}}.  {{ message.msg }}
                </div>
             </div>
          </div>

          <!-- Here we are going to the box to add messages -->
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_message()">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>

               <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Message "
                    v-model="message"
                  />
                </div>
              </div>

              <div class="field" v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
              <button class="button is-success">Submit Message</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default{
  name: "MessageBox",
  data(){
    return{
      message: '',
      error_message: '',
    }
  },
  methods:{
    submit_message(){
      if(this.message){
        // if these exists then we are going to submit the product
        axios.post('admin_panel/message_box/post/',{
          msg: this.message
        }, {headers: {Authorization: `Bearer ${this.accessToken}`}}).then(()=>{
          this.messageboxes.push({msg: this.message})
          this.message = ''
        }).catch(err=>{
          console.log(err.response.data.msg)
          this.error_message = err.response.data.msg[0]
        })
      }
    }
  },
  computed:{
    ...mapState(['messageboxes', 'accessToken'])
  },
  created(){
    console.log(this.messageboxes)
  }
}
</script>
