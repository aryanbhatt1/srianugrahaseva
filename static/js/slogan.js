const audioControButton = document.querySelectorAll(".play__pause");

function playPauseAudio(btn, track) {
  if (track.paused) {
    track.play();
    btn.classList.add("pause");
    btn.classList.remove("play");
  } else {
    track.pause();
    btn.classList.add("play");
    btn.classList.remove("pause");
  }
}

// Loop all instance of play buttons
if (audioControButton.length > 0) {
  audioControButton.forEach((playButton) => {
    playButton.addEventListener("click", (e) => {
      e.preventDefault;
      let elemContainer = playButton.parentElement;
      let track = elemContainer.querySelector("audio");
      stopAllAudio(track);
      playPauseAudio(playButton, track);
    });
  });
}

function stopAllAudio(elem) {
  const audios = document.getElementsByTagName("audio");
  for (var i = 0, len = audios.length; i < len; i++) {
    if (audios[i] != elem) {
      audios[i].pause();
      console.log(audios[i].nextElementSibling);
      audios[i].nextElementSibling.classList.remove("pause");
      audios[i].nextElementSibling.classList.add("play");
    }
  }
}

