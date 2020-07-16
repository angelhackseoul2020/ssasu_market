<template>
  <div class="adminStoreAddWrap">
    <div class="adminStoreAdd">
      <form action method="GET">
        <label for="storeName">상점 이름</label>
        <input type="text" id="storeName" placeholder="상점 이름" required />

        <label for="storeAddress">주소</label>
        <input type="text" id="storeAddress" placeholder="주소" />

        <label for="storeTell">연락처</label>
        <input type="text" id="storeTell" placeholder="연락처" />

        <label for="storeMemo">메모</label>
        <input type="text" id="storeMemo" placeholder="메모" />

        <div class="deleteSave">
          <button type="submit" id="delete">delete</button>
          <button type="submit" id="save">save</button>
        </div>
      </form>
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
.adminStoreAddWrap {
  margin: 3rem 3rem;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.adminStoreAdd {
}
label {
  display: block;
  width: 100%;
  font-size: 12px;
  line-height: 16px;
}
input {
  width: 300px;
  height: 50px;
  font-size: 2rem;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
input:focus,
input:hover,
input:active {
  outline: none;
  box-shadow: none;
  border-color: #f3c0d8;
}
button {
  width: 100px;
  height: 40px;
  font-size: 1.3rem;
  text-align: center;
  border-style: none;
  border-radius: 40px;
  cursor: pointer;
}
#delete {
  background-color: rgb(156, 4, 4);
}
#save {
  background-color: #26833d;
}
</style>