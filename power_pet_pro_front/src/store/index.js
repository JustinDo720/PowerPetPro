import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    latestProducts: "", // we are going to use this state to store our 5 products in case we need to use it elsewhere
  },
  mutations: {
    // mutations have state as their parameters as they're the only ones that could actually change state
    grabLatestProducts(state, latestProductsProxy) {
      // We do get the proxy but we want to make sure we throw in an object to our latestProducts state
      state.latestProducts = latestProductsProxy.latestProductsProxy;
    },
  },
  actions: {
    // actions have context to access things like states but they can't change them unless you perform action (commit)
  },
  modules: {},
});
