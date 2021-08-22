import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    latestProducts: "", // we are going to use this state to store our 5 products in case we need to use it elsewhere
    cart:{
      items:[]
    },
    isAuthenticated: false,
    accessToken: '',
    isLoading: false // We are going to add a loading bar for things that are loading
  },
  mutations: {
    // mutations have state as their parameters as they're the only ones that could actually change state
    grabLatestProducts(state, latestProductsProxy) {
      // We do get the proxy but we want to make sure we throw in an object to our latestProducts state
      state.latestProducts = latestProductsProxy.latestProductsProxy;
    },
    initializeStore(state){
      if(localStorage.getItem('cart')){
        // If cart exist then we will set our state to the cart
        // We use JSON.parse to grab an object wrapped in strings because of Local Storage
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        // NOTE: Localstorage usually takes strings thats why we need stringify to wrap our obj in string format
        // we dont have cart in our localstorage so lets set it
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    // Let's go ahead and make a function that changes the cart items
    addToCart(state, item){
      // check if item exist in cart if so we will just increase quantity
      const exists = state.cart.items.filter(cart_item => cart_item.id === item.id)

      // We need to make sure that exists[0].quantity is a number we could add or else we get NaN
      if(exists[0].quantity === null){
        exists[0].quantity = 0 // setting exists to 0 will give us a number to add with quantity
      }

      if(exists.length){ // if the length is bigger than 0 which means the product is already there then we increase quantity
        console.log(`Before Quantity: ${exists[0].quantity} & Item Quantity: ${item.item.quantity}`)
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.item.quantity)
        console.log(`After Quantity: ${exists[0].quantity} & Item Quantity: ${item.quantity}`)
      }else{
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  actions: {
    // actions have context to access things like states but they can't change them unless you perform action (commit)
  },
  modules: {},
});
