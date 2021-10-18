<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.get_image" />
        </figure>
        <h1 class="title">
          {{ product.name }}
        </h1>
        <p>
          {{ product.description }}
        </p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Information</h2>
        <p><strong>Price: </strong>${{ product.price }}</p>
        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" v-model="quantity" />
          </div>
          <div class="control">
            <button class="button is-primary" @click="addToCart()">
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
// toast is like messages in django + bootstrap
import { toast } from "bulma-toast";

export default {
  name: "Product",
  data() {
    return {
      quantity: 1,
      product: {},
    };
  },
  methods: {
    // we want to make sure getProduct is async before setIsLoading false will come before our axios request
    async getProduct() {
      this.$store.commit("setIsLoading", true);
      // These params are set in router using /:category_slug/:product_slug
      // The reason why we want these slugs is because we will use them to access our ProductDetail API
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;
      await axios
        .get(`/product_list/product_detail/${category_slug}/${product_slug}/`)
        .then((response) => {
          this.product = response.data;
        });
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };
      // now we also need to pass in the current_cart
      const current_cart_ids = JSON.parse(
        localStorage.getItem("cart")
      ).items.map((item) => item.product.id);
      console.log(current_cart_ids);
      this.$store.commit("addToCart", {
        item_object: item,
        current_cart: current_cart_ids,
      });

      // once we add our item then lets toast
      toast({
        message: "The Product was added to your cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000, // milliseconds
        position: "bottom-right",
      });
    },
  },
  created() {
    // getProduct will grab the route params --> Category Slug and Product Slug
    this.getProduct();
  },
};
</script>
