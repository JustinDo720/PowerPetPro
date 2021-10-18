<template>
  <section class="hero has-background-grey-lighter is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <figure class="image is-2by1">
          <img src="../assets/ppp_logo2.jpg" />
        </figure>
        <div class="box p-6 has-background-grey-dark">
          <p class="title has-text-light">
            Your Account has been <strong>ACTIVATED</strong>!
          </p>
          <p class="subtitle has-text-light">
            Thank you for activating your account. Please continue logging in
            <router-link :to="{ name: 'Login' }" class="has-text-primary"
              ><u>here</u></router-link
            >
            or head to Account then Log In
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "Activate",
  computed: {},
  created() {
    const uid = this.$route.params.uid;
    const token = this.$route.params.token;

    axios.post("auth/users/activation/", {
      uid: uid,
      token: token,
    });
  },
};
</script>
