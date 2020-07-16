<template>
  <div class="admin">
      <Nav class="Nav"></Nav>
      <router-view class="adminRouter" />
  </div>
</template>

<script>
import Nav from "../components/admin/Nav.vue";
export default {
    name: "Admin",
    components: {
        Nav
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.admin {
    background: url('../assets/imgs/bgimg.png') center/cover no-repeat;
    height: 100vh;
    display: flex;
}

.Nav {
    width: 16%;
}

.adminRouter {
    width: 84%;
}
</style>