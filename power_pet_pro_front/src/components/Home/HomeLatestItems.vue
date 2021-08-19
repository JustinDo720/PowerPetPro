<template>
  <div class="section">
    <h1 class="title is-size-2 has-text-centered">
      Latest Products
    </h1>
    <!-- This component shows the 5 latest products-->
    <div class="columns">
      <div class="column" v-for="(product, index) in latestProducts.results" :key="index">
        <div class="card">
          <div class="card-image" v-if="product.get_thumbnail">
            <figure class="image is-4by3">
              <!-- We need to bind src to use product in the tag. Dont use image or get_image use thumbnail -->
              <img :src="product.get_thumbnail" alt="Product image">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">{{ product.name }}</p>
                <p class="subtitle is-6">{{ product.category_name }}</p>
              </div>
            </div>

            <div class="content">
              {{ product.limited_description }}...
              <a href="#">
                View Details
              </a>
            </div>
            <footer class="card-footer">
              <button class="button is-primary">
                <span class="icon is-small">
                  <i class="fas fa-plus"></i>
                </span>
                <span>
                  Add To Cart
                </span>
              </button>
            </footer>
          </div>
        </div>
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