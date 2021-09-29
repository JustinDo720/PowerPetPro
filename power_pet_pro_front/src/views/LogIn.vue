<template>
  <section class="hero is-fullheight is-success">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">
          Login
        </p>
        <hr>
        <p class="subtitle">
          Please login to proceed.
        </p>

        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="login">
              <figure class="image is-128x128 is-inline-block">
                <img class="is-square" alt="ppp-logo" src="../assets/ppp_logo.jpg">
              </figure>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                        <i class="far fa-user-circle"></i>
                  </span>
                  <input class="input is-medium" type="text" placeholder="Username or Email" v-model="login_field">
                </div>
              </div>

              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="********" v-model="login_password">
                </div>
              </div>

              <div v-if="error_message">
                 <p class="is-danger help">
                  {{ error_message }}
                </p>
                <p class="has-text-info help">
                  {{ warning_message }}
                </p>
              </div><br>


              <button class="button is-success">Sign in</button>
              <div>
                <p>
                  New to the website?
                  <router-link :to="{name:'Register'}" class="has-text-info">
                    Create an account here!
                  </router-link>
                </p>
                <p>
                  Need a new activation link?
                  <router-link :to="{name:'Reactivate'}" class="has-text-info">
                    Resend activation code here!
                  </router-link>
                </p>
                <p>
                  <router-link :to="{name:'ResetPassword'}" class="has-text-info">
                    Forgot Password?
                  </router-link>
                </p>

              </div>
            </form>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default{
  name:'Login',
  data(){
    return{
       login_field: '',
       login_password:'',
       error_message: '',
       warning_message: ''
    }
  },
  methods:{
    login(){
      if(this.login_field && this.login_password){
        axios.post('api/token/',{
        username: this.login_field, // We really only need this because our UserAccountManager takes username || email
        password: this.login_password
      }).then((response)=>{
            this.$store.commit('loginUser',{
            username: response.data.username,
            user_id: response.data.user_id,
            accessToken: response.data.access,
            refreshToken: response.data.refresh
          })
          this.$router.push({name:'Home'})
        }).catch((err)=>{
          if(err){
            this.error_message = err.response.data.detail
            this.warning_message = 'Have you activated your account? Please check your email for the activation link.'
          }
        })
      }else{
        this.error_message = 'Please enter in your username or email and your password'
      }

    }
  }

}
</script>

<style scoped>
hr{
  width:50%;
  margin: 0 auto;
  color: black;
}
</style>
