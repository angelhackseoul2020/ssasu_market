<template>
  <div class="adminStoreWrap">
    <div class="adminStore">
      <div class="header">
        <button type="submit" class="ddStore">상점 추가</button>

        <button type="submit" class="addStore">상점 추가</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminStore",
  components: {}
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.adminStoreWrap {
  margin: 3rem 3rem;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
}
.header {
  display: flex;
  background-color: pink;
  justify-content: flex-end;
}
.addStore {
  background-color: #fdafd063;
  outline: 0;
  width: 130px;
  font-size: 1.6rem;
  color: #2e0202;
  border-style: none;
  border-radius: 40px;
}
.addStore:hover {
  cursor: pointer;
}
</style>