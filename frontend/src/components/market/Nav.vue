<template>
  <div class="nav">
    <router-link style="text-decoration: none; color: inherit;" to="/market/home">
      <div class="home">
        <img class="homeIcon" src="../../assets/imgs/marketHome.png" alt />홈
      </div>
    </router-link>
    <router-link style="text-decoration: none; color: inherit;" to="/market/store">
      <div class="store">
        <img class="storeIcon" src="../../assets/imgs/marketStore.png" alt />상점
      </div>
    </router-link>
    <router-link style="text-decoration: none; color: inherit;" to="/market/community">
      <div class="community">
        <img class="communityIcon" src="../../assets/imgs/marketCommunity.png" alt />게시판
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Nav"
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.nav {
  background-color: #fdafd063;
  border-right: 1px solid rgba(143, 141, 141, 0.534);
  font-family: "Jua", sans-serif;
  color: #2e0202;
  text-align: center;
}

.home {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.homeIcon {
  width: 140px;
}
.store {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.storeIcon {
  width: 140px;
}
.community {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.communityIcon {
  width: 130px;
}
</style>
