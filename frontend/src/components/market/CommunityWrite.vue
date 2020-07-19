<template>
  <div class="communityWriteWrap">
    <div class="communityWrite">
      <input class="photoInput" type="file" @change="imgPreview"/>
      <img src="#" alt="" id="imgPreview">
      <div class="textUpload">
        <input type="text" class="title" placeholder="제목" />
        <textarea name id cols="30" rows="10" class="textField" placeholder="본문"></textarea>
        <button class="write" type="submit">
          <img class="writeIcon" src="../../assets/imgs/write.png" alt />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommunityWrite",
  methods:{
    imgPreview(event){
      var imgUrl = URL.createObjectURL(event.target.files[0])
      var img = document.getElementById('imgPreview')
      img.src = imgUrl
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
.communityWriteWrap {
  margin: 3rem 3rem;
  display: flex;
  align-items: center;
}
.communityWrite {
  position: relative;
  width: 70%;
  margin: 0 auto;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
  display: flex;
  justify-content: center;
  padding: 1rem 0;
  /* height: 400px; */
}
.photoUpload {
  /* margin-top: 30px; */
}
.photoInput {
}
.textUpload {
  display: flex;
  flex-direction: column;
  align-items: center;
}
input {
  font-size: 1.3rem;
  color: #3d0606b7;
}
input::placeholder {
  font-size: 1.3rem;
  color: #5a0909b7;
}
input:focus {
  outline: none;
}
textarea {
  font-size: 1.3rem;
  color: #3d0606b7;
}
textarea::placeholder {
  font-size: 1.3rem;
  color: #5a0909b7;
}
textarea:focus {
  outline: none;
}
.title {
  background-color: #fdafd063;
  border-radius: 13px;
  border: none;
  margin: 3% 0;
  width: 300px;
  height: 40px;
}
.textField {
  background-color: #fdafd063;
  border-radius: 13px;
  border: none;
  width: 300px;
  height: 200px;
}
.write {
  border-style: none;
  background-color: transparent;
  outline: 0;
  width: 50px;
  margin-top: 3%;
}
.write:hover {
  cursor: pointer;
}
.writeIcon {
  width: 50px;
}
#imgPreview{
  position: absolute;
  top: 60px;
  left: 70px;
  width: 300px;
  height: 200px;
}
</style>