<template>
  <div class="reviewDetailWrap">
    <button class="backbtn">
      <img src="../../assets/imgs/back.png" alt="뒤로가기" />
    </button>
    <div class="reviewDetail">
      <div class="reviewTitle">오전에 광장시장 다녀왔는데</div>
      <div class="reviewPhoto">
        <img src="../../assets/imgs/logo1.png" alt="사진" />
      </div>
      <div class="reviewText">오전에 한복 사러 광장시장 갔는데 사람..</div>
      <div class="reviewStar">5.0 ★★★★★</div>
      <div id="reviewer">2020.07.12 Seolyu</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewDetail"
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.reviewDetailWrap {
  margin: 3rem 3rem;
  display: flex;
  align-items: center;
}
.backbtn {
  display: block;
  background-color: transparent;
  border: 0;
  outline: 0;
}
.reviewDetail {
  width: 70%;
  margin: 0 auto;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 1rem 5rem;
  /* height: 400px; */
}
.reviewTitle {
  font-size: 2rem;
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