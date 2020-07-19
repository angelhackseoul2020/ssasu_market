<template>
  <div class="reviewDetailWrap">
    <div class="reviewDetail">
      <button @click="close" class="closebtn">
        <!-- <button class="closebtn"> -->
        <img class="closebtnImg" src="../../assets/imgs/close.png" alt="닫기" />
      </button>
      <div class="reviewTitle">{{data.title}}</div>
      <div class="reviewPhoto">
        <img src="../../assets/imgs/logo1.png" alt="사진" />
      </div>
      <div class="reviewText">{{data.text}}</div>
      <div class="reviewStar">{{data.score}} {{data.star}}</div>
      <div id="reviewer">2020.07.12 Seolyu</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewDetail",
  methods: {
    close() {
      this.$emit("closeModal");
    }
  },
  props: {
    data: {
      type: Object
    }
  },
  data() {
    return {};
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.reviewDetailWrap {
  /* position: fixed; */
  margin: 1.5rem 0;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.closebtn {
  align-self: flex-end;
  display: block;
  background-color: transparent;
  border: 0;
  outline: 0;
}
.closebtn:hover {
  cursor: pointer;
  transform: scale(1.1);
}
.closebtnImg {
  width: 30px;
}
.reviewDetail {
  width: 70%;
  /* margin: 0 auto; */
  margin-left: 170px;
  background-color: rgba(252, 252, 252);
  border-radius: 15px;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 1rem 5rem;
  border: 5px solid transparent;
  /* height: 400px; */
}
.reviewDetail:hover {
  border: 5px solid rgba(206, 21, 123, 0.295);
}
.reviewTitle {
  font-size: 2.5rem;
  text-align: center;
}
.reviewPhoto {
  width: 400px;
}
.reviewPhoto img {
  width: 100%;
}
.reviewText {
  font-size: 1.4rem;
  align-self: flex-start;
}
.reviewStar {
  font-size: 1.3rem;
  align-self: flex-start;
}
#reviewer {
  font-size: 1.2rem;
  color: rgb(37, 156, 37);
  align-self: flex-end;
}
</style>