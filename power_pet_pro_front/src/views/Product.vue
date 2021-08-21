<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
            <img :src="product.get_image">
        </figure>
        <h1 class="title">
          {{ product.name }}
        </h1>
        <p>
          {{ product.description }}
        </p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">
          Information
        </h2>
        <p>
          <strong>Price: </strong>${{ product.price }}
        </p>
        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" v-model="quantity">
          </div>
          <div class="control">
            <button class="button is-primary">
              <span class="icon is-small">
                <i class="fas fa-plus"></i>
              </span>
              <span> Add To Cart </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default{
  name:'Product',
  data(){
    return{
      quantity: 1,
      product:{},
    }
  },
  methods:{
    getProduct(){
      // These params are set in router using /:category_slug/:product_slug
      // The reason why we want these slugs is because we will use them to access our ProductDetail API
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug
      axios.get(`product_detail/${category_slug}/${product_slug}/`).then((response)=>{
        console.log(response.data)
        this.product = response.data
      })

    }
  },
  created(){
    // getProduct will grab the route params --> Category Slug and Product Slug
    this.getProduct()
  }

}
</script>