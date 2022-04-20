<template>
  <div>
    <div class="columns is-multiline" :class="{'is-centered': !product.get_image}">
      <div class="column is-9" v-if="product.get_image">
        <div class="container">
          <figure>
            <p class="image mb-6 image is-16by9">
              <img :src="product.get_image" />
            </p>
          </figure>
        </div>

      </div>

      <div class="column"
           :class="{'is-3': product.get_image, 'has-text-centered': !product.get_image, 'is-half': !product.get_image}">
        <div class="content box has-background-info has-text-white mr-2">
          <h1 class="title has-text-white">
            {{ product.name }}
          </h1>
          <div class="box has-background-primary">
            <p>
              {{ product.description }}
            </p>
          </div>

          <h4 class="title is-4">
            <strong>Price: </strong>
            <span class="has-text-danger-dark">
              ${{ product.price }}
            </span>
          </h4>
          <div :class="{'columns': !product.get_image, 'is-centered': !product.get_image}">
            <div :class="{'column':!product.get_image, 'is-half':!product.get_image}">
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

      if (this.product.get_image) {
        this.product["photo"] = this.product.get_image;
      }
      const item = {
        product: this.product,
        quantity: this.quantity,
      };
      // now we also need to pass in the current_cart
      const current_cart_ids = JSON.parse(
        localStorage.getItem("cart")
      ).items.map((item) => item.product.id);
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
