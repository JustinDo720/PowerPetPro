<template>
   <section class="hero is-fullheight is-warning">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">
          Reset Password Confirmation
        </p>
        <hr>
        <p class="subtitle">
          Please enter your new password!
        </p>

          <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_password">
              <figure class="image is-128x128 is-inline-block">
                <img class="is-square" alt="ppp-logo" src="../assets/ppp_logo.jpg">
              </figure>
               <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="New Password" v-model="new_password">
                </div>
              </div>
               <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="Confirm Password" v-model="confirm_password">
                </div>
              </div>

              <div v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div><br>

              <button class="button is-warning" type="submit">Reset Password</button>
            </form>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast';

export default{
  name: "ResetPasswordConfirmation",
  data(){
    return{
       new_password: '',
       confirm_password: '',
       uid: null,
       token: null,
       error_message: '',
    }
  },
  methods:{
    submit_password(){
      console.log(this.uid, this.token)
      if(this.new_password && this.confirm_password && this.new_password === this.confirm_password){
       axios.post('auth/users/reset_password_confirm/',{
         uid: this.uid,
         token: this.token,
         new_password: this.new_password,
         re_new_password: this.confirm_password
       }).then(response=>{
         console.log(response)
         toast({
            message: 'Your password has been reset!!!!',
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 60000, // milliseconds
            position: "bottom-right",
          });
         this.$router.push({name: 'Home'})
       }).catch(err=>{
         this.error_message = err.response.data[0]
       })
      } else if(this.new_password === '' || this.confirm_password === ''){
        this.error_message = 'Please enter in your new password or confirmation password'
      } else{
        this.error_message = 'Your new password and confirmation password does not match'
      }

    }
  },
  beforeMount(){
    this.uid = this.$route.params.uid
    this.token = this.$route.params.token
  }
}
</script>