<template>
  <div class="reviewCardWrap">
    <div class="reviewCard">
      <div class="reviewPhoto">
        <img src="../../assets/imgs/logo1.png" alt="사진" />
      </div>
      <div class="reviewInfo">
        <div class="reviewTitle">{{title}}</div>
        <div class="reviewText">{{text}}</div>
        <div class="reviewStar">{{score}} {{star}}</div>
        <div id="reviewer">2020.07.12 Seolyu</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewCard",
  props: {
    title: {
      type: String
    },
    text: {
      type: String
    },
    score: {
      type: Number
    },
    star: {
      type: String
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.reviewCard {
  width: 100%;
  height: 220px;
  padding: 30px;
  display: flex;
  background-color: rgba(255, 255, 255, 0.829);
  border-radius: 15px;
  border: 2px solid transparent;
  margin-top: 1.5rem;
}
.reviewCard:hover {
  background-color: rgb(253, 250, 252);
  border: 2px solid rgba(218, 101, 165, 0.795);
}
.reviewPhoto {
  width: 30%;
  height: 150px;
  overflow: hidden;
}
.reviewPhoto img {
  width: 100%;
}
.reviewInfo {
  width: 70%;
  padding: 10px 10px 10px 40px;
}
.reviewTitle {
  font-size: 2rem;
}
.reviewText {
  font-size: 1.4rem;
}
.reviewStar {
  font-size: 1.3rem;
}
#reviewer {
  font-size: 1.2rem;
  color: rgb(37, 156, 37);
  text-align: right;
}
</style>