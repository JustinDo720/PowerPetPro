<template>
  <div id="nav">
    <MessageBar class="mb-3 p-4"></MessageBar>
    <NavBar></NavBar>
    <router-view />
    <div class="is-loading-bar has-text-centered" :class="{'is-loading': this.isLoading}">
      <div class="lds-dual-ring">
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import NavBar from "./components/NavBar";
import MessageBar from "./components/MessageBar";
import Footer from "./components/Footer";
import { mapState } from 'vuex';
import bulmaQuickview from "bulma-quickview/src/js";

export default {
  components: {
    NavBar,
    MessageBar,
    Footer,
  },
  computed:{
    ...mapState(['isLoading'])
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
  },
  mounted(){
    var quickviews = bulmaQuickview.attach(); // quickviews now contains an array of all Quickview instances
  }
};
</script>

<style lang="scss">
@import '../node_modules/bulma';
@import '~bulma';
@import '~bulma-quickview';


.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
