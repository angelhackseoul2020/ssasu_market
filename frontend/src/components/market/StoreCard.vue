<template>
    <div class="storeCardWrap">
        <div class="storeCard">
            <div class="storePhoto">
                <img src="../../assets/imgs/logo1.png" alt="사진" />
            </div>
            <div class="storeInfo">
            <div class="storeNameCategory">
                <div class="storeName">신라한복</div>
                <div class="storeCategory">/ 한복</div>
            </div>
            <div class="storeAddress">서울특별시 종로구 예지도 6-1 광장시장 1층 134-1호</div>
            <div class="storePhone">02-2275-9003</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "StoreCard"
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.storeCard {
    width: 100%;
    height: 220px;
    padding: 30px;
    display: flex;
    background-color: rgba(255, 255, 255, 0.829);
    border-radius: 15px;
    border: 2px solid transparent;
    margin-top: 1.5rem;
}
.storeCard:hover {
    background-color: rgb(253, 250, 252);
    border: 2px solid rgba(218, 101, 165, 0.795);
}
.storePhoto {
    width: 30%;
    height: 150px;
    overflow: hidden;
}
.storePhoto img {
    width: 100%;
}
.storeInfo {
    padding: 10px 10px 10px 40px;
}
.storeNameCategory {
  display: flex;
}
.storeName {
  font-size: 2rem;
  margin-right: 30px;
}
.storeCategory {
  font-size: 1.5rem;
}
.storeAddress {
  font-size: 1.3rem;
  margin-bottom: 4px;
}
.storePhone {
  font-size: 1.2rem;
  color: rgb(37, 156, 37);
}
</style>