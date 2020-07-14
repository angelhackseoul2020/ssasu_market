<template>
  <div class="nav">
      <div class="home">홈</div>
      <div class="store">상점</div>
      <div class="community">게시판</div>
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