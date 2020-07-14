<template>
  <div class="nav">
      <router-link style="text-decoration: none; color: inherit;" to="/market/home"><div class="home">홈</div></router-link>
      <router-link style="text-decoration: none; color: inherit;" to="/market/store"><div class="store">상점</div></router-link>
      <router-link style="text-decoration: none; color: inherit;" to="/market/community"><div class="community">게시판</div></router-link>
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

.home {
    height: 33.3vh;
    line-height: 33.3vh;
    border-bottom: 1px solid rgba(143, 141, 141, 0.534);
}
.store {
    height: 33.3vh;
    line-height: 33.3vh;
    border-bottom: 1px solid rgba(143, 141, 141, 0.534);
}
.community{
    height: 33.3vh;
    line-height: 33.3vh;
}
</style>