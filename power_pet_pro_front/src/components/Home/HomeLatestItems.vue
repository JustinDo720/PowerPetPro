<template>
  <div class="section">
    <h1 class="title is-size-2 has-text-centered">Latest Products</h1>
    <!-- This component shows the 5 latest products-->
    <div class="columns">
      <div
        class="column"
        v-for="(product, index) in latestProducts.results"
        :key="index"
      >
        <div class="card">
          <div class="card-image" v-if="product.get_thumbnail">
            <a href="#" @click="viewDetails(product.get_absolute_url)">
              <figure class="image is-4by3">
                <!-- We need to bind src to use product in the tag. Dont use image or get_image use thumbnail -->
                <img :src="product.get_thumbnail" alt="Product image" />
              </figure>
            </a>

          </div>
          <div class="card-content has-text-centered">
            <div class="media">
              <div class="media-content">
                <a href="#" @click="viewDetails(product.get_absolute_url)">
                  <p class="title is-3" >{{ product.name }}</p>
                </a>
                <p class="subtitle is-6 tag is-light is-rounded mt-5">{{ product.category_name }}</p>
              </div>
            </div>

            <div class="content">
              <span class="subtitle is-4">
                ${{ product.price }}
              </span>
            </div>
            <!-- We just need to wrap the card with columns and the inner html is a column itself and then boom center -->
            <div class="columns is-multiline">
              <footer class="card-footer column has-text-centered is-half is-offset-one-quarter">
                <button class="button is-primary" @click="addToCart(product)">
                  <span class="icon is-small">
                    <i class="fas fa-plus"></i>
                  </span>
                  <span> Add To Cart </span>
                </button>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

export default {
  name: "HomeLatestItems",
  data() {
    return {
      // NOTE: http:// is necessary or else Uncaught (in promise) Error: Network Error
      apiURL: "http://localhost:8000/product_list/",
    };
  },
  computed: {
    ...mapState(["latestProducts"]),
  },
  methods:{
    viewDetails(product_abs_url){
      console.log(product_abs_url)
      let product_url = '/product_detail' + product_abs_url
      console.log(product_url)
      // what we want to do is push to our product url. the product_abs_url is like: /category_slug/product_slug/
      this.$router.push(product_url)
    },
    addToCart(storeItem){
      this.$store.commit('addToCart', {item: storeItem})
    }
  },
  mounted() {
    axios.get(this.apiURL).then((response) => {
      this.$store.commit("grabLatestProducts", {
        latestProductsProxy: response.data,
      });
    });
  },
};
</script>

<style scoped></style>
