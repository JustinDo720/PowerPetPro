<template>
  <table class="table is-striped is-fullwidth is-hoverable">
    <thead>
      <tr>
        <th>Product Name</th>
        <th>Category Name</th>
        <th>Price</th>
        <th>Limited Description</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(product, index) in products" :key="index">
        <th>
          <router-link :to="productUrl(product.get_absolute_url)">
            {{ product.name }}
          </router-link>
        </th>
        <th>{{ product.category_name }}</th>
        <th>{{ product.price }}</th>
        <th>{{ product.limited_description }}</th>
        <th>
          <button
            class="button is-warning is-ghost"
            @click="edit_mode_activated(product)"
          >
            <i class="fas fa-pencil-alt"></i></button
          >&nbsp;
          <button
            class="button is-danger is-ghost"
            @click="delete_mode_activated(product)"
          >
            <i class="fas fa-trash"></i>
          </button>
        </th>
      </tr>
    </tbody>
  </table>
  <nav class="pagination is-centered" role="navigation" aria-label="pagination">
    <button class="pagination-previous" @click="changeView(previous)">
      Previous
    </button>
    <button class="pagination-next" @click="changeView(next)">Next page</button>
    <ul class="pagination-list">
      <li>
        <div class="box">Total Items: {{ totalProductCount }}</div>
      </li>
      <li>
        <div class="box">Current Page: {{ currPage }}</div>
      </li>
    </ul>
  </nav>

  <!-- Edit Modal -->
  <div class="modal" :class="{ 'is-active': edit_mode }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Edit Product</p>
        <button
          class="delete"
          aria-label="close"
          @click="edit_mode = !edit_mode"
        ></button>
      </header>
      <section class="modal-card-body">
        <!-- Content ... -->
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success">Save changes</button>
        <button class="button" @click="edit_mode = !edit_mode">Cancel</button>
      </footer>
    </div>
  </div>

  <!-- Delete Modal -->
  <div class="modal" :class="{ 'is-active': delete_mode }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm Delete Product</p>
        <button
          class="delete"
          aria-label="close"
          @click="delete_mode = !delete_mode"
        ></button>
      </header>
      <div class="modal-card-body">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3" v-if="chosen_product_picture">
              <img :src="chosen_product_picture" alt="Product-Image" />
            </figure>
          </div>
          <div class="card-content has-text-centered">
            <p class="title is-4">
              {{ chosen_product_name }}
            </p>
            <p class="subtitle is-6">${{ chosen_product_price }}</p>
          </div>

          <div class="content">
            <div class="box">
              {{ chosen_product_description }}
            </div>
          </div>
        </div>
      </div>
      <footer class="modal-card-foot">
        <button class="button is-danger" @click="delete_product()">
          Delete Product
        </button>
        <button class="button" @click="delete_mode = !delete_mode">
          Cancel
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js";
import { mapState } from "vuex";
import { toast } from "bulma-toast";

export default {
  name: "ViewAllProducts",
  data() {
    return {
      products: [],
      next: "",
      previous: "",
      totalProductCount: null,
      currPage: null,
      edit_mode: false,
      delete_mode: false,
      // Product chosen by admin
      chosen_product_id: null,
      chosen_product_picture: null,
      chosen_product_name: null,
      chosen_product_description: null,
      chosen_product_price: null,
      chosen_product_productUrl: null,
    };
  },
  computed: {
    ...mapState(["accessToken"]),
  },
  methods: {
    productUrl(abs_url) {
      return `/product_list/product_detail${abs_url}`;
    },
    changeView(url) {
      if (url !== null) {
        axios
          .get(url, {
            headers: { Authorization: `Bearer ${Cookies("accessToken")}` },
          })
          .then((response) => {
            this.products = response.data.results;
            this.next = response.data.next;
            this.previous = response.data.previous;
            this.totalProductCount = response.data.count;
            this.currPage = parseInt(response.data.next.slice(-1)) - 1;
          });
      }
    },
    edit_mode_activated(product) {
      this.edit_mode = !this.edit_mode;
      this.chosen_product_id = product.id;
      this.chosen_product_picture = product.image;
      this.chosen_product_name = product.name;
      this.chosen_product_description = product.description;
      this.chosen_product_price = product.price;
    },
    delete_mode_activated(product) {
      this.delete_mode = !this.delete_mode;
      this.chosen_product_id = product.id;
      this.chosen_product_picture = product.image;
      this.chosen_product_name = product.name;
      this.chosen_product_description = product.description;
      this.chosen_product_price = product.price;
      this.chosen_product_productUrl = this.productUrl(
        product.get_absolute_url
      );
      console.log(this.chosen_product_productUrl);
    },
    delete_product() {
      axios
        .delete(`admin_panel/product_list/update/${this.chosen_product_id}/`, {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        .then((response) => {
          toast({
            message: response.data.success,
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
          this.delete_mode = !this.delete_mode;
        });
    },
  },
  created() {
    axios
      .get("product_list/", {
        headers: { Authorization: `Bearer ${Cookies("accessToken")}` },
      })
      .then((response) => {
        this.products = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
        this.totalProductCount = response.data.count;
        this.currPage = parseInt(response.data.next.slice(-1)) - 1;
      });
  },
};
</script>
