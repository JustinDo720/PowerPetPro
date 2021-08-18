<template>
  <div class="section">
    <h1 class="title is-size-2 has-text-centered">
      Latest Products
    </h1>
    <!-- This component shows the 5 latest products-->
    <div class="columns">
      <div class="column" v-for="(product, index) in latestProducts.results" :key="index">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{ product.name }}</p>
              </div>
            </div>

            <div class="content">
              {{ product.description }}
            </div>
            <footer class="card-footer">
               <p>Category: {{ product.category_name }}</p>
            </footer>
          </div>
        </div>
        {{ product }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from "axios";

export default{
  name:'HomeLatestItems',
  data(){
    return{
      // NOTE: http:// is necessary or else Uncaught (in promise) Error: Network Error
      apiURL: 'http://localhost:8000/product_list/',
    }
  },
  computed: {
    ...mapState([
      'latestProducts'
    ])
  },
  mounted(){
    axios.get(this.apiURL).then((response)=>{
      console.log(response.data)
      this.$store.commit('grabLatestProducts', {latestProductsProxy:response.data})
    })
  }

}
</script>

<style scoped></style>