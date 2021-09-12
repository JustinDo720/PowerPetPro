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
            <form class="box">
              <figure class="image is-128x128 is-inline-block">
                <img class="is-square" alt="ppp-logo" src="../assets/ppp_logo.jpg">
              </figure>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                        <i class="far fa-user-circle"></i>
                  </span>

                  <input class="input is-medium" type="email" placeholder="e.g. alex@example.com">
                </div>
              </div>

              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input class="input is-medium" type="password" placeholder="********">
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

}
</script>

<style scoped>
hr{
  width:50%;
  margin: 0 auto;
  color: black;
}
</style>
