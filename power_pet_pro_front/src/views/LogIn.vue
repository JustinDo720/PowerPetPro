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
                  <input class="input is-medium" type="text" placeholder="Username" v-model="login_username">
                </div>
              </div>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                        <i class="far fa-user-circle"></i>
                  </span>

                  <input class="input is-medium" type="email" placeholder="e.g. alex@example.com" v-model="login_email">
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

              <button class="button is-success">Sign in</button>
            </form>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<script>

export default{
  name:'Login',
  data(){
    return{
       login_username: '',
       login_email:'',
       login_password:'',
    }
  },
  methods:{
    login(){
      this.$store.dispatch('loginUser', {
        username: this.login_username,
        email: this.login_email,
        password: this.login_password
      }).then(()=>{
        this.$router.push({name:'Home'})
      })
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
