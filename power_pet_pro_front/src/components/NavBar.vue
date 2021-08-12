<template>
  <nav class="navbar is-transparent extended-navbar has-shadow is-dark">
    <div id="navbarExampleTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href="https://bulma.io/">
          Shop
        </a>
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link" href="https://bulma.io/documentation/overview/start/">
            About Us
          </a>
          <div class="navbar-dropdown is-boxed">
            <a class="navbar-item" href="https://bulma.io/documentation/overview/start/">
              Our Mission
            </a>
            <a class="navbar-item" href="https://bulma.io/documentation/overview/modifiers/">
              Our Shelter
            </a>
            <a class="navbar-item" href="https://bulma.io/documentation/columns/basics/">
              What makes us different
            </a>
            <a class="navbar-item" href="https://bulma.io/documentation/layout/container/">
              Layout
            </a>
            <a class="navbar-item" href="https://bulma.io/documentation/form/general/">
              Form
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item" href="https://bulma.io/documentation/elements/box/">
              Elements
            </a>
            <a class="navbar-item is-active" href="https://bulma.io/documentation/components/breadcrumb/">
              Components
            </a>
          </div>
        </div>
      </div>

      <div class="navbar-brand">
      <a href="/">
        <img src="../assets/ppp_logo2.jpg" alt="Power Pet Pro Logo" class="is-rounded" width="112" height="28">
      </a>
      <div class="navbar-burger" data-target="navbarExampleTransparentExample">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field is-grouped">
            <div class="control has-icons-left has-icons-right">
              <input class="input" type="text" placeholder="Search">
              <span class="icon is-small is-left">
                <i class="fas fa-search"></i>
              </span>
              </div>
            </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>

export default{
  name: 'NavBar'
}
</script>

<style scoped>

.extended-navbar{
  font-size: 1.125rem;
  padding: 1rem 4rem;
}
</style>