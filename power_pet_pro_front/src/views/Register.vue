<template>
  <section class="hero is-fullheight is-info">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">
          Register
        </p>
        <hr>
        <p class="subtitle">
          Please register to login.
        </p>

          <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="register">
              <figure class="image is-128x128 is-inline-block">
                <img class="is-square" alt="ppp-logo" src="../assets/ppp_logo.jpg">
              </figure>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                        <i class="far fa-user-circle"></i>
                  </span>
                  <input class="input is-medium" type="text" placeholder="Username" v-model="register_username">
                </div>
              </div>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                         <i class="fas fa-envelope"></i>
                  </span>
                  <input class="input is-medium" type="email" placeholder="Email" v-model="register_email">
                </div>
              </div>

              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="********" v-model="register_password">

                </div>
              </div>
               <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="Confirm Password" v-model="register_repassword">
                </div>
              </div>
              <div v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
              <button class="button is-info" type="submit">Register</button>
            </form>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
import { toast } from "bulma-toast";
import axios from 'axios';

export default{
  name:'Register',
  data(){
    return{
      register_username: '',
      register_email: '',
      register_password: '',
      register_repassword: '',
      password_not_matched: false,
      error_message: '',
    }
  },
  methods:{
    register(){
      if(this.register_username && this.register_email && this.register_password && this.register_password === this.register_repassword){
        axios.post("auth/users/",{
          username: this.register_username,
          email: this.register_email,
          password: this.register_password,
          re_password: this.register_repassword
        }).then(()=>{
          toast({
            message: "Please check your email to confirm!!!",
            type: "is-warning",
            dismissible: true,
            pauseOnHover: true,
            duration: 60000, // milliseconds
            position: "bottom-right",
          });
          this.$router.push({name:'Home'})
        }).catch(err=>{
          for(let error_message in err.response.data){
            this.error_message = err.response.data[error_message][0]
          }
        })
      }else{
        this.password_not_matched = true
      }

    },
  },

}
</script>

<style scoped>
hr{
  width:50%;
  margin: 0 auto;
  color: black;
}
</style>
