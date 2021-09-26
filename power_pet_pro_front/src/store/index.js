import { createStore } from "vuex";
import axios from "axios";
import Cookies from 'cookies-js';

// We will use this function to save our tokens
function saveTokens(username, accessToken, refreshToken) {
  Cookies.set('username', username, { expires: 604800});
  Cookies.set('accessToken', accessToken, { expires: 604800});
  Cookies.set('refreshToken', refreshToken, { expires: 604800});
}

export default createStore({
  state: {
    latestProducts: "", // we are going to use this state to store our 5 products in case we need to use it elsewhere
    cart: {
      items: [],
    },
    isAuthenticated: false,
    username:"",
    user_id: null,
    accessToken: "",
    refreshToken: "",
    isLoading: false, // We are going to add a loading bar for things that are loading
    searchTerm: "",
    testMessage: {},
  },
  mutations: {
    // mutations have state as their parameters as they're the only ones that could actually change state
    grabLatestProducts(state, latestProductsProxy) {
      // We do get the proxy but we want to make sure we throw in an object to our latestProducts state
      state.latestProducts = latestProductsProxy.latestProductsProxy;
    },
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        // If cart exist then we will set our state to the cart
        // We use JSON.parse to grab an object wrapped in strings because of Local Storage
        state.cart = JSON.parse(localStorage.getItem("cart"));
      } else {
        // NOTE: Localstorage usually takes strings thats why we need stringify to wrap our obj in string format
        // we dont have cart in our localstorage so lets set it
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }

      if (Cookies.get('username') && Cookies.get('accessToken') && Cookies.get('refreshToken')){
        const username = Cookies('username')
        const accessToken = Cookies('accessToken')
        const refreshToken  = Cookies('refreshToken')

        axios.post('/auth/jwt/verify/', {
          token: accessToken
        }).then(()=>{
            state.username = username
            state.accessToken = accessToken
            state.refreshToken = refreshToken

            saveTokens(state.username, state.accessToken, state.refreshToken)

        }).catch(()=>{
          axios.post('/api/token/refresh/',{
            refresh: refreshToken
          }).then((response)=>{
            console.log(response.data.access)
            state.username = username
            state.accessToken = response.data.access
            state.refreshToken = response.data.refresh // this is possible because of rotating refresh in settings

            saveTokens(state.username, state.accessToken, state.refreshToken)
          })
        })
      }
    },
    // Let's go ahead and make a function that changes the cart items
    addToCart(state, item_object) {
      let item = item_object.item_object // this will allow us to just access products or quantity must easier

      // We want to check if the product exist using the ids.
      const exists = state.cart.items.filter(cart_item => cart_item.product.id === item.product.id)
      // if our exists has a length > 0 that means the product exist and we need to handle that
      if(exists.length){
        // each time the product exists we are incrementing our quantity for a specific product instead of adding same
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity) // exists[0].quantity = total quant
      }else{
        // this is a new product so we want to just push this to our cart
        state.cart.items.push(item)
      }

      // regardless of exists, we need to update our localstorage cart with state card for initializeStore
      localStorage.setItem("cart", JSON.stringify(state.cart));

    },
    // Now we could use setIsLoading for where we want to load usually before our api request because it takes some time
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    addSearch(state, searchTerm){
      state.searchTerm = searchTerm.searchTerm;
    },
    loginUser(state, {username, accessToken, refreshToken, user_id}){
      state.username = username
      state.accessToken = accessToken
      state.refreshToken = refreshToken
      state.user_id = user_id

      saveTokens(state.username, state.accessToken, state.refreshToken)
    },
    logoutUser(state){
      state.username = ''
      state.accessToken = ''
      state.refreshToken = ''

      Cookies.expire('username')
      Cookies.expire('accessToken')
      Cookies.expire('refreshToken')
    }
  },
  actions: {},
  modules: {},
  getters: {
    isAuth(state){
      return state.accessToken !== ''
    }
  },
});
