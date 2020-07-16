<template>
  <div class="nav">
      <router-link style="text-decoration: none; color: inherit;" to="/admin/store"><div class="store">상점</div></router-link>
      <router-link style="text-decoration: none; color: inherit;" to="/admin/user"><div class="user">유저</div></router-link>
  </div>
</template>

<script>
export default {
    name: "Nav"
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.nav {
    background-color: #fdafd063;
    border-right: 1px solid rgba(143, 141, 141, 0.534);
    font-family: "Jua", sans-serif;
    font-size: 3rem;
    color: #2E0202;
    text-align: center;
}

.store {
    height: 50vh;
    line-height: 50vh;
    border-bottom: 1px solid rgba(143, 141, 141, 0.534);
}
.user {
    height: 50vh;
    line-height: 50vh;
    border-bottom: 1px solid rgba(143, 141, 141, 0.534);
}
</style>