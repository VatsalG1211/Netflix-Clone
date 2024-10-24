let menu_wrapper = document.getElementById('menu_wrapper');
let account_menu = document.querySelector('.account-menu');
let account_menu_wrap = document.querySelector('.account-menu-wrap');
let account_div = document.querySelector('.account');
let account = document.getElementById('usrname');
let searchbar = document.getElementById('searchbar');
let searchbtn = document.getElementById('search');
let closesearch = document.getElementById('close-search');


let searchbar_wrapper = document.getElementById('search-bar');
let searchicon = document.getElementById('search-icon');



let html_ = document.querySelector('html')

let main_tag = document.querySelector('main')
let header_tag = document.querySelector('header')
let footer_tag = document.querySelector('footer')


window.addEventListener("scroll", () => {
  menu_wrapper.classList.remove('open_menu');
  const header = document.querySelector('header')
  if (window.innerWidth > 500) {
    header.classList.toggle('active', window.scrollY > 100);
  }

})


// Search Integration

$(searchbar_wrapper).ready(function () {

  const search_wrapper = document.querySelector('.search-content')
  $(search_wrapper).hide()
  $('#no-result').hide();
  const search_pannels = document.querySelectorAll('.searched-content-panel')
  const Newpanel = `<div class="searched-content-panel"
  style="gap:10px;align-content: center;margin-bottom: 50px;display: flex;justify-content:flex-start;padding:0px 80px;flex-shrink:0;"></div>`


  function debounce(func, delay) {
    let debounceTimeout;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(() => func.apply(context, args), delay);
    };
}


  // Defining Search Functionality

  function performSearch()
  {


    // pop Closes onclicking main_tag while popwindow is Opened  
    search_wrapper.addEventListener("click", () => {
      if (pop_movie.classList.contains('active')) {
        closePopWindow();
      }
    })
    
    
        $(search_wrapper).show()
        $('#no-result').hide();
    
        // Check Window Size and confirm limit of searched content in one panel
        let searched_content_limit;
        if(window.innerWidth>1520)
        {
          searched_content_limit = 6
        }
        else if(window.innerWidth<1540 && window.innerWidth>1300)
          {
            searched_content_limit = 5
          }
          else if(window.innerWidth<1300 && window.innerWidth>1060)
            {
              searched_content_limit = 4
            }
            else if(window.innerWidth<1060 && window.innerWidth>780)
              {
                searched_content_limit = 3
              }
              console.log("search limit",searched_content_limit)
    
    
    
        $('.searched-content-panel').remove()
        search_wrapper.insertAdjacentHTML('beforeend', Newpanel)
    
    
        query = $(this).val().trim();
    
    
        console.log("query -> ", query)
    
    
    
    
        if (query != "") {
    
          $('main').hide()
    
          fetch(`/search/${query}`)
            .then(response => response.json())
            .then(data => {
              console.log(data);
    
              if (data.length == 0) {
                console.log("No season Found")
                $('#no-result').show();
              }
    
    
    
    
    
    
              for (let i = 1; i <= data.length; i++) {
    
    
                if (data[i - 1].c_type == "series") {
    
    
                  post = `
            <div class="post-wrap" data-season-id="${data[i - 1].c_id}">
                  
                  <div class="movie-posters" style="background-image: url('${data[i - 1].poster}');">
                      <div class="vid-btn">
      
                      </div>
                      <div class="additional-detail">
                          <div class="pops-btn-addit">
                              <form>
                                  <a href="/content/series/${data[i - 1].episodes[0].id}" class="i-mod"
                                      style="padding: 5px 10px;padding-top: 9px;"><i class="fa-solid fa-play"></i></a>
                              </form>
                              
                              <form method="post" class="addlistform">
                                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                  <label>
                                      <input type="hidden" class="c_id" name="c_id" value="${data[i - 1].c_id}">
                                     
                                      ${data[i - 1].is_in_content_list ? `<a class="i-mod add_list bgchange" data-season-id="${data[i - 1].c_id}"><i
                                              class="fa-solid fa-check"></i></a>` : `<a class="i-mod add_list" data-season-id="${data[i - 1].c_id}"><i
                                              class="fa-solid fa-plus"></i></a>` }
                                  </label>
                              </form>
      
                              <form method="post" class="addlikeform">
                                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                  <label>
                                      <input type="hidden" class="c_id" name="c_id" value="${data[i - 1].c_id}">
      
                                      
                                      ${data[i - 1].is_in_liked_list ? ` <a class="i-mod add_like bgchange" data-season-id="${data[i - 1].c_id}"><i
                                              class="fa-solid fa-thumbs-up" style="transform: translateY(-2.5px);"></i></a>`
                      : `<a class="i-mod add_like" data-season-id="${data[i - 1].c_id}"><i
                                              class="fa-solid fa-thumbs-up" style="transform: translateY(-2.5px);"></i></a>`
                    }
                                  </label>
                              </form>
                              <form>
                                  <a class="i-mod pop-btn" style="position: relative;left: 220%;">
                                      <i style="transform: rotate(90deg) translate(-3px,0px) scaleY(1.5);font-size: 0.8rem;width:18px;"
                                          class="fa-solid fa-greater-than" style="font-size: 0.5rem;"></i>
                                  </a>
                              </form>
      
      
                          </div>
                          <div class="episode-short-detail">
                              
                              <a style="font-weight:400;">${data[i - 1].series} </a><span style="font-weight:600;">Season
                                  ${data[i - 1].season_no} </span>
                          </div>
      
                      </div>
      
                  </div>
              </div>
            
            `
                }
    
                else {
    
                  post = `
              <div class="post-wrap" data-season-id="${data[i - 1].c_id}">
                    
                    <div class="movie-posters" style="background-image: url('${data[i - 1].poster}');">
                        <div class="vid-btn">
        
                        </div>
                        <div class="additional-detail">
                            <div class="pops-btn-addit">
                                <form>
                                    <a href="/content/movie/${data[i - 1].m_id}" class="i-mod"
                                        style="padding: 5px 10px;padding-top: 9px;"><i class="fa-solid fa-play"></i></a>
                                </form>
                                
                                <form method="post" class="addlistform">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                    <label>
                                        <input type="hidden" class="c_id" name="c_id" value="${data[i - 1].c_id}">
                                       
                                        ${data[i - 1].is_in_content_list ? `<a class="i-mod add_list bgchange" data-season-id="${data[i - 1].c_id}"><i
                                                class="fa-solid fa-check"></i></a>` : `<a class="i-mod add_list" data-season-id="${data[i - 1].c_id}"><i
                                                class="fa-solid fa-plus"></i></a>` }
                                    </label>
                                </form>
        
                                <form method="post" class="addlikeform">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                    <label>
                                        <input type="hidden" class="c_id" name="c_id" value="${data[i - 1].c_id}">
        
                                        
                                        ${data[i - 1].is_in_liked_list ? ` <a class="i-mod add_like bgchange" data-season-id="${data[i - 1].c_id}"><i
                                                class="fa-solid fa-thumbs-up" style="transform: translateY(-2.5px);"></i></a>`
                      : `<a class="i-mod add_like" data-season-id="${data[i - 1].c_id}"><i
                                                class="fa-solid fa-thumbs-up" style="transform: translateY(-2.5px);"></i></a>`
                    }
                                    </label>
                                </form>
                                <form>
                                    <a class="i-mod pop-btn" style="position: relative;left: 220%;">
                                        <i style="transform: rotate(90deg) translate(-3px,0px) scaleY(1.5);font-size: 0.8rem;width:18px;"
                                            class="fa-solid fa-greater-than" style="font-size: 0.5rem;"></i>
                                    </a>
                                </form>
        
        
                            </div>
                            <div class="episode-short-detail">
                                
                                <a style="font-weight:400;">${data[i - 1].title} </a>
                            </div>
        
                        </div>
        
                    </div>
                </div>
              
              `
    
    
                }
    
    
                if ((i - 1) % searched_content_limit == 0) {
                  search_wrapper.insertAdjacentHTML('beforeend', Newpanel)
                }
    
                let new_search_panel_all = search_wrapper.querySelectorAll('.searched-content-panel')
                let last_search_panel = new_search_panel_all[new_search_panel_all.length - 1]
    
                last_search_panel.insertAdjacentHTML('beforeend', post)
    
    
    
              }
    
    
              let m_posters = search_wrapper.querySelectorAll('.movie-posters')
    
    
    
    
              m_posters.forEach(poster => {
                const vid_det = poster.querySelector('.vid-btn');
                const additional_pop = poster.querySelector('.additional-detail');
                const pop_btn = additional_pop.querySelector('.pop-btn');
                const postWrap = poster.parentElement;
    
                pop_btn.addEventListener("click", () => {
    
                  OpenPopWindow(postWrap);
    
                });
    
    
                poster.addEventListener("click", () => {
    
                  if (window.innerWidth <= 1100) {
                    poster.style.scale = '1.0';
    
                  }
                  else {
                    poster.style.scale = '1.40';
                    poster.style.marginRight = '5px';
    
    
                  }
    
                  vid_det.style.opacity = '100%';
                  additional_pop.style.display = 'block';
                  postWrap.style.zIndex = '1';
    
    
    
                  poster.addEventListener("mouseleave", () => {
                    poster.style.scale = '1';
                    poster.style.margin = '0';
                    vid_det.style.opacity = '0%';
                    postWrap.style.zIndex = '0';
                    additional_pop.style.display = 'none';
    
                  });
    
                });
    
    
                // In Additional Btn in Content List in Searching
    
                $(poster).ready(function () {
    
                  let addlistbtn = poster.querySelector('.add_list')
    
    
                  $(addlistbtn).on('click', function () {
    
    
    
                    var c_id = addlistbtn.getAttribute('data-season-id');
    
                    console.log(c_id);
    
                    $.ajax({
                      url: '/content/add_my_list/', // Ensure this URL is correct
                      type: 'POST',
                      data: {
                        'c_id': c_id // Send c_id as part of form data
                      },
                      headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
                      success: function (response) {
                        console.log(response); // Handle success
                      },
                      error: function (error) {
                        console.error(error); // Handle error
                      }
                    });
    
                    const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)
    
                    same_poster_list.forEach(same_poster => {
    
                      let addlistbtns = same_poster.querySelector('.add_list')
    
    
                      if (addlistbtns.children[0].classList.contains('fa-plus')) {
                        addlistbtns.children[0].classList.remove('fa-plus')
                        addlistbtns.children[0].classList.add('fa-check')
                        addlistbtns.classList.toggle('bgchange')
                      }
                      else {
                        addlistbtns.children[0].classList.remove('fa-check')
                        addlistbtns.children[0].classList.add('fa-plus')
                        addlistbtns.classList.toggle('bgchange')
                      }
    
    
                    })
    
    
    
                  });
                });
    
    
    
                // In Additional Btn in Like List in Searching
    
                $(poster).ready(function () {
    
                  let addlikebtn = poster.querySelector('.add_like')
    
    
                  $(addlikebtn).on('click', function () {
    
    
    
                    var c_id = addlikebtn.getAttribute('data-season-id');
    
    
                    $.ajax({
                      url: '/content/add_like/', // Ensure this URL is correct
                      type: 'POST',
                      data: {
                        'c_id': c_id // Send c_id as part of form data
                      },
                      headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
                      success: function (response) {
                        console.log(response); // Handle success
                      },
                      error: function (error) {
                        console.error(error); // Handle error
                      }
                    });
    
    
                    const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)
    
                    same_poster_list.forEach(same_poster => {
    
                      let addlikebtns = same_poster.querySelector('.add_like')
    
                      addlikebtns.classList.toggle('bgchange')
    
                    })
                  });
                });
              });
            })
        }


  }


  // 


  $(searchbar).on("input",debounce(performSearch,500));


})






// 







menu_wrapper.addEventListener("mouseleave", () => {

  setTimeout(() => {
    menu_wrapper.classList.remove('open_menu');
  }, 200)

});








function toogleMenu() {
  menu_wrapper.classList.add('open_menu');

}

function toogleSearch() {
  searchbar.classList.toggle('open-search');
  if (searchbar.classList.contains('open-search')) {
    searchbar.focus()
  }
  else {
    searchbar.blur()
  }

  searchbtn.classList.toggle('button-pos');
  closesearch.classList.toggle('visible');
  searchbar_wrapper.classList.toggle('move-search-input');
  searchicon.classList.toggle('i-pos');
}

function closeSearch() {
  if (searchbar.value != "") {
    searchbar.value = ""
    return
  }
  $('.searched-content-panel').remove()
  $('main').show();
  toogleSearch()
}








// POP Movie

const pop_movie = document.querySelector('.pop-movie');
const pop_close = pop_movie.querySelector('.pop-close');
const playerIframe = pop_movie.querySelector('.plyr__video-embed');
const mutebtn = pop_movie.querySelector("#mute");



// Clearing POP Window Info
function clearInfo_popWindow() {

  if (mutebtn.children[0].classList.contains('fa-volume-xmark')) {
    mutebtn.children[0].classList.remove('fa-volume-xmark')
    mutebtn.children[0].classList.add('fa-volume-high')
  }


  // Content List Reset
  let addlistbtn = pop_movie.querySelector('.add_list')
  if (addlistbtn.children[0].classList.contains('fa-check')) {
    addlistbtn.children[0].classList.add('fa-plus')
    addlistbtn.children[0].classList.remove('fa-check')
    addlistbtn.classList.toggle('bgchange')
  }

  // Like Btn Reset

  let addlikebtn = pop_movie.querySelector('.add_like')
  if (addlikebtn.classList.contains('bgchange')) {
    addlikebtn.classList.toggle('bgchange')
  }

  let trailer = pop_movie.querySelector('.plyr__video-embed');
  trailer.querySelector('iframe').remove();



  const season_dropdown = pop_movie.querySelectorAll('.seasons option')
  season_dropdown.forEach(option => option.remove());

  const episodes = pop_movie.querySelectorAll('.episode');
  episodes.forEach(episode => episode.remove());

  const actors = pop_movie.querySelector('#actor');
  actors.textContent = ''

  const genres = pop_movie.querySelector('#genres');
  genres.textContent = ''
}



// Fetching Content

async function fetchContent(c_id) {

  fetch(`/content/get_content/${c_id}`)
    .then(response => response.json())
    .then(data => {

      console.log(data);






      // const playerIframe = pop_movie.querySelector('.plyr__video-embed')
      playerIframe.innerHTML = `<iframe src="${data.trailer}" allow="autoplay; encrypted-media"></iframe>`;



      // Initialize Plyr after setting the src
      const player = new Plyr('#player', {
        autoplay: true,
        muted: false,
        controls: [],
        youtube: {
          noCookie: true  // Optional: Use YouTube's privacy-enhanced mode
        }
      });





      mutebtn.addEventListener("click", () => {

        if (player.muted) {
          // If muted, unmute it and change the button text
          player.muted = false;
          if (mutebtn.children[0].classList.contains('fa-volume-xmark')) {
            mutebtn.children[0].classList.remove('fa-volume-xmark')
            mutebtn.children[0].classList.add('fa-volume-high')
          }


        } else {
          // If not muted, mute it and change the button text
          player.muted = true;

          if (mutebtn.children[0].classList.contains('fa-volume-high')) {
            mutebtn.children[0].classList.remove('fa-volume-high')
            mutebtn.children[0].classList.add('fa-volume-xmark')
          }

        }

        console.log(player)

      })


      // PlayBtn
      let playBtn = pop_movie.querySelector('#play-btn2')
      if (data.c_type == 'series') {
        playBtn.href = `/content/series/${data.episodes[0].id}`;
      }
      else {
        playBtn.href = `/content/movie/${data.m_id}`;
      }




      // Add Content List Btn

      let addlistbtn = pop_movie.querySelector('.add_list')

      if (data.is_in_content_list) {
        addlistbtn.children[0].classList.remove('fa-plus')
        addlistbtn.children[0].classList.add('fa-check')
        addlistbtn.classList.add('bgchange')
      }


      // 

      // Add Like Btn

      let addlikebtn = pop_movie.querySelector('.add_like')

      if (data.is_in_liked_list) {

        addlikebtn.classList.toggle('bgchange')
      }


      // 





      // player on Title Img

      let movie_logo = pop_movie.querySelector('.movie-logo img')
      movie_logo.src = data.title_img
      console.log(data.title_img)
      //  

      // content info
      const releasedDate = new Date(data.released_date);
      const year = releasedDate.getFullYear();

      let released_date = pop_movie.querySelector('#released_date')
      released_date.textContent = `${year}`;

      if (data.c_type == "series") {
        let no_of_seasons = pop_movie.querySelector('#total_seasons');
        no_of_seasons.textContent = `${data.total_seasons} Seasons`;
      }


      // Content Title and Season if it is series

      let title_name = pop_movie.querySelector('#content-title');
      if (data.c_type == "series") {
        title_name.textContent = `${data.series}`;
        title_name.nextElementSibling.textContent = `Season ${data.season_no}`;
      }
      else {
        title_name.textContent = `${data.title}`;

      }

      // Description
      let description = pop_movie.querySelector('#description')
      description.textContent = `${data.description}`
      // 

      // Actors

      let actors = pop_movie.querySelector('#actor')
      data.actors.forEach(actor => {
        let element = document.createElement('span')
        element.textContent = actor.name + ', '

        actors.appendChild(element)


      })


      // 

      // Genres

      let genres = pop_movie.querySelector('#genres')
      let genres_length = data.genres.length

      for (let i = 1; i <= genres_length; i++) {
        let element = document.createElement('span')
        if (i == genres_length) {
          element.textContent = data.genres[i - 1].name
        }
        else {
          element.textContent = data.genres[i - 1].name + ', '
        }
        genres.appendChild(element)
      }

      // If Content is Movie

      let episodes_wrapper = pop_movie.querySelector('.episode-wrapper')

      if (data.c_type == "movie") {
        episodes_wrapper.style.display = 'none';
      }
      else {
        episodes_wrapper.style.display = 'block';

        //  Season Drop Down

        const season_dropdown = pop_movie.querySelector('.seasons')
        console.log(season_dropdown);

        for (let i = 1; i <= data.total_seasons; i++) {
          let option;
          if (data.season_no == i) {
            option = `<option value="${data.seasons[i - 1]}" selected>Season ${i}</option>`;
          }
          else {
            option = `<option value="${data.seasons[i - 1]}">Season ${i}</option>`;
          }

          season_dropdown.insertAdjacentHTML('beforeend', option);
        }



        //  Episodes



        for (let i = 1; i <= data.episodes.length; i++) {

          episode = `<div class="episode">
            <span style="color: white;font-size: 1.5rem;">${i}</span>
            <div class="thumbnail"
                style="background-image: url('${data.episodes[i - 1].thumbnail}');">
                <a href="/content/series/${data.episodes[i - 1].id}"><i class="fa-solid fa-play"></i></a>
            </div>
            <div class="epi-info-wrapper">
                <div class="episode-name">
                    <span style="color: white;font-size: 0.9rem;font-weight: 550;">${data.episodes[i - 1].name}</span>
                    <span style="color: rgb(106,106,106);font-size: 0.9rem;font-weight: 400;">55m</span>
                </div>
                <div class="episode-description">
                    <a style="color: rgb(106, 106, 106);font-size: 0.8rem;">${data.episodes[i - 1].description}</a>
                </div>
            </div>
            </div>
            `
          episodes_wrapper.insertAdjacentHTML('beforeend', episode)

        }


      }



    })


}

async function fetchEpisodes(c_id) {

  fetch(`/content/get_episodes/${c_id}`)
    .then(response => response.json())
    .then(data => {

      console.log(data);


      //  Episodes

      let episodes_wrapper = pop_movie.querySelector('.episode-wrapper')

      for (let i = 1; i <= data.episodes.length; i++) {

        episode = `<div class="episode">
          <span style="color: white;font-size: 1.5rem;">${i}</span>
          <div class="thumbnail"
              style="background-image: url('${data.episodes[i - 1].thumbnail}');">
              <a href="/content/series/${data.episodes[i - 1].id}"><i class="fa-solid fa-play"></i></a>
          </div>
          <div class="epi-info-wrapper">
              <div class="episode-name">
                  <span style="color: white;font-size: 0.9rem;font-weight: 550;">${data.episodes[i - 1].name}</span>
                  <span style="color: rgb(106,106,106);font-size: 0.9rem;font-weight: 400;">55m</span>
              </div>
              <div class="episode-description">
                  <a style="color: rgb(106, 106, 106);font-size: 0.8rem;">${data.episodes[i - 1].description}</a>
              </div>
          </div>
          </div>
          `
        episodes_wrapper.insertAdjacentHTML('beforeend', episode)

      }



    }
    )

}


// Open Pop Movie 

function OpenPopWindow(i) {

  const c_id = i.getAttribute('data-season-id');

  const addlistbtn = pop_movie.querySelector('.add_list')
  addlistbtn.setAttribute('data-season-id', c_id)

  const input_c_id = pop_movie.querySelector('.addlistform .c_id')
  input_c_id.value = c_id



  const addlikebtn = pop_movie.querySelector('.add_like')
  addlikebtn.setAttribute('data-season-id', c_id)

  const input_c_id_like = pop_movie.querySelector('.addlikeform .c_id')
  input_c_id_like.value = c_id


  // Fetching Content 

  fetchContent(c_id);

  // 





  // Disable pointer events for all elements
  document.querySelectorAll('.movie-posters').forEach(item => {
    item.style.pointerEvents = 'none';
  })

  document.querySelectorAll('.prev-btn').forEach(item => {
    item.style.pointerEvents = 'none';
  })

  document.querySelectorAll('.next-btn').forEach(item => {
    item.style.pointerEvents = 'none';
  })

  document.querySelectorAll('.detail-btn').forEach(item => {
    item.style.pointerEvents = 'none';
  })



  // Set styles for the popup
  html_.style.overflow = 'hidden';
  header_tag.style.pointerEvents = 'none';
  header_tag.querySelector('.navbar').style.opacity = '50%';
  main_tag.style.opacity = '50%';

  pop_movie.classList.toggle('active');



}







// pop Closes onclicking main_tag while popwindow is Opened  
main_tag.addEventListener("click", () => {
  if (pop_movie.classList.contains('active')) {
    closePopWindow();
  }
})



// Closing Pop Window

function closePopWindow() {
  clearInfo_popWindow();

  main_tag.style.opacity = '100%';
  header_tag.querySelector('.navbar').style.opacity = '100%';

  
  

  // Enable pointer events for all elements
  document.querySelectorAll('.movie-posters, .prev-btn, .next-btn, .detail-btn').forEach(item => {
    item.style.pointerEvents = 'all';
  });

  html_.style.overflow = 'auto';
  header_tag.style.pointerEvents = 'all';
  footer_tag.style.pointerEvents = 'all';
  header_tag.style.zIndex = '8000';

  // Reset popup styles
  pop_movie.classList.toggle('active')
}



// Close popup-movie
pop_close.addEventListener("click", () => {

  closePopWindow()
  if(listWrapper)
    {
      listWrapper.style.pointerEvents = 'all';
    }
  
});



const more_info_btn = document.getElementById('info-btn')

if(more_info_btn!=null)
{
  more_info_btn.addEventListener("click", () => {
    OpenPopWindow(more_info_btn);
  });
}



// AJAX Dropdown Integration
$(pop_movie).ready(function () {

  var selectedOption = $(pop_movie.querySelector('.seasons')).val();


  $(".seasons").change(function () {
    var season = $(this).val();

    // clearInfo_popWindow();
    const episodes = pop_movie.querySelectorAll('.episode');
    episodes.forEach(episode => episode.remove());
    $('#loading-indicator').show();

    setTimeout(() => {
      $('#loading-indicator').hide();
      // Fetch episodes for the selected season
      fetchEpisodes(season).then(() => {
      })
    }, 400);



  });
});

// 
// ***  Drop Down Completes  ***

// In POP Window Content List 
$(pop_movie).ready(function () {

  let addlistbtn = pop_movie.querySelector('.add_list')
  var c_id;

  $(pop_movie.querySelector('.addlistform .c_id')).on('click', function () {
    c_id = $(this).val();



    if (addlistbtn.children[0].classList.contains('fa-plus')) {
      addlistbtn.children[0].classList.remove('fa-plus')
      addlistbtn.children[0].classList.add('fa-check')
      addlistbtn.classList.toggle('bgchange')
    }
    else {
      addlistbtn.children[0].classList.remove('fa-check')
      addlistbtn.children[0].classList.add('fa-plus')
      addlistbtn.classList.toggle('bgchange')
    }

    console.log(addlistbtn)
    console.log(c_id);
    $.ajax({
      url: '/content/add_my_list/', // Ensure this URL is correct
      type: 'POST',
      data: {
        'c_id': c_id // Send c_id as part of form data
      },
      headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
      success: function (response) {
        console.log(response); // Handle success
      },
      error: function (error) {
        console.error(error); // Handle error
      }
    });



    const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)

    same_poster_list.forEach(same_poster => {

      let addlistbtns = same_poster.querySelector('.add_list')


      if (addlistbtns.children[0].classList.contains('fa-plus')) {
        addlistbtns.children[0].classList.remove('fa-plus')
        addlistbtns.children[0].classList.add('fa-check')
        addlistbtns.classList.toggle('bgchange')
      }
      else {
        addlistbtns.children[0].classList.remove('fa-check')
        addlistbtns.children[0].classList.add('fa-plus')
        addlistbtns.classList.toggle('bgchange')
      }
    })
  });

});
// 
// *** Content List Adding Completes  ***





// In POP Window Adding Like 
$(pop_movie).ready(function () {

  let addlikebtn = pop_movie.querySelector('.add_like')
  var c_id;

  $(pop_movie.querySelector('.addlikeform .c_id')).on('click', function () {
    c_id = $(this).val();

    console.log("CLicked Like Button")

    addlikebtn.classList.toggle('bgchange')


    $.ajax({
      url: '/content/add_like/', // Ensure this URL is correct
      type: 'POST',
      data: {
        'c_id': c_id // Send c_id as part of form data
      },
      headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
      success: function (response) {
        console.log(response); // Handle success
      },
      error: function (error) {
        console.error(error); // Handle error
      }
    });



    const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)

    same_poster_list.forEach(same_poster => {

      let addlikebtn = same_poster.querySelector('.add_like')

      addlikebtn.classList.toggle('bgchange')
    })

  });

});

// 
// *** Adding Like Content Completes ***













//  /// ////       ///////////////////////  ////

// Adding Like and Content in list from Outside of Pop Window 


posters = document.querySelectorAll('.movie-posters')

posters.forEach(poster => {


  // In Additional Btn in Content List

  $(poster).ready(function () {

    let addlistbtn = poster.querySelector('.add_list')


    $(addlistbtn).on('click', function () {



      var c_id = addlistbtn.getAttribute('data-season-id');

      console.log(c_id);

      $.ajax({
        url: '/content/add_my_list/', // Ensure this URL is correct
        type: 'POST',
        data: {
          'c_id': c_id // Send c_id as part of form data
        },
        headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
        success: function (response) {
          console.log(response); // Handle success
        },
        error: function (error) {
          console.error(error); // Handle error
        }
      });

      const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)

      same_poster_list.forEach(same_poster => {

        let addlistbtns = same_poster.querySelector('.add_list')


        if (addlistbtns.children[0].classList.contains('fa-plus')) {
          addlistbtns.children[0].classList.remove('fa-plus')
          addlistbtns.children[0].classList.add('fa-check')
          addlistbtns.classList.toggle('bgchange')
        }
        else {
          addlistbtns.children[0].classList.remove('fa-check')
          addlistbtns.children[0].classList.add('fa-plus')
          addlistbtns.classList.toggle('bgchange')
        }


      })



    });
  });



  // In Additional Btn in Like List

  $(poster).ready(function () {

    let addlikebtn = poster.querySelector('.add_like')


    $(addlikebtn).on('click', function () {



      var c_id = addlikebtn.getAttribute('data-season-id');


      $.ajax({
        url: '/content/add_like/', // Ensure this URL is correct
        type: 'POST',
        data: {
          'c_id': c_id // Send c_id as part of form data
        },
        headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
        success: function (response) {
          console.log(response); // Handle success
        },
        error: function (error) {
          console.error(error); // Handle error
        }
      });


      const same_poster_list = document.querySelectorAll(`.post-wrap[data-season-id="${c_id}"]`)

      same_poster_list.forEach(same_poster => {

        let addlikebtns = same_poster.querySelector('.add_like')

        addlikebtns.classList.toggle('bgchange')



      })




    });
  });



})





// ///// /// // ///////////////////////   ////

















// Slider Movie

let sliders_wrap = document.querySelectorAll('.slider-wrapper');


sliders_wrap.forEach(item => {
  const sliderWrapper = item

  if (sliderWrapper.querySelectorAll('.popular-rank-number').length > 0) {
    const popular_content_rank_span = sliderWrapper.querySelectorAll('.popular-rank-number')

    const no_10th_popular = popular_content_rank_span[popular_content_rank_span.length - 1]

    no_10th_popular.style.transform = 'translate(-25px,-155px)';
  }



  let slider_wrapper_length = sliderWrapper.offsetWidth - 200;

  window.addEventListener("resize", () => {
    slider_wrapper_length = sliderWrapper.offsetWidth - 200;
    console.log("Changed size", slider_wrapper_length)

    console.log("slider movie", movie_list_wrapper.offsetWidth)
  })

  const prevBtn = item.querySelector('.prev-btn');
  const nextBtn = item.querySelector('.next-btn');
  const movie_list_wrapper = item.querySelector('.slider-movie'); // Single element

  // Access the movie list (all 'post-wrap' elements inside the wrapper)
  const movie_list = movie_list_wrapper.querySelectorAll('.post-wrap');

  item.addEventListener("mouseenter", () => {
    prevBtn.style.opacity = '1';
    nextBtn.style.opacity = '1';
  })

  item.addEventListener("mouseleave", () => {
    prevBtn.style.opacity = '0';
    nextBtn.style.opacity = '0';
  })


  let counter = 0;



  movie_list.forEach(i => {
    let posters = i.querySelectorAll('.movie-posters');
    let postWrap = i  // Post-Wrap


    posters.forEach(poster => {
      const vid_det = poster.querySelector('.vid-btn');
      const additional_pop = poster.querySelector('.additional-detail');
      const pop_btn = additional_pop.querySelector('.pop-btn');





      // ON clicking view more btn to pop-up full window
      pop_btn.addEventListener("click", () => {

        OpenPopWindow(i);

      });


      const whole_slider_wrapper = sliderWrapper.parentElement;

      poster.addEventListener("click", () => {

        if (window.innerWidth <= 1100) {
          poster.style.scale = '1.25';
          poster.style.marginRight = '5px';
          postWrap.style.zIndex = '7001';
          whole_slider_wrapper.style.zIndex = '1';

        }
        else {
          poster.style.scale = '1.50';
          poster.style.marginRight = '15px';
          postWrap.style.zIndex = '7001';
          whole_slider_wrapper.style.zIndex = '1';
        }

        if (sliderWrapper.querySelectorAll('.popular-rank-number').length > 0) {
          poster.style.width = '225px';
          poster.style.height = '128px';
          poster.style.transform = 'translateX(0px)';
          poster.style.backgroundSize = '225px 128px';
        }


        vid_det.style.opacity = '100%';
        additional_pop.style.display = 'block';

        // postWrap.classList.toggle('margin-toggle');



        poster.addEventListener("mouseleave", () => {
          poster.style.scale = '1';
          poster.style.margin = '0';
          vid_det.style.opacity = '0%';
          postWrap.style.zIndex = '0';
          whole_slider_wrapper.style.zIndex = '0';

          // postWrap.classList.toggle('margin-toggle');

          additional_pop.style.display = 'none';


          if (sliderWrapper.querySelectorAll('.popular-rank-number').length > 0) {
            poster.style.width = '178px';
            poster.style.height = '115px'
            poster.style.transform = 'translateX(45px)';;
            poster.style.backgroundSize = '178px 115px';
          }


        });

      });



    })


  })



  let no_of_content = movie_list.length;
  // console.log("No of Content",no_of_content)
  let currentPosition = 0;
  let currentPage = 1




  let limit_visibility_content;


  if (slider_wrapper_length <= 1200 && slider_wrapper_length >= 900) {
    limit_visibility_content = 5;
  }
  else if (slider_wrapper_length <= 900 && slider_wrapper_length >= 716) {
    limit_visibility_content = 4;
  }
  else if (slider_wrapper_length <= 716 && slider_wrapper_length >= 490) {
    limit_visibility_content = 3;
  }
  else if (slider_wrapper_length <= 490 && slider_wrapper_length >= 260) {
    limit_visibility_content = 2;
  }
  else if (slider_wrapper_length > 1200) {
    limit_visibility_content = 6;
  }

  console.log("Limit of Visibility",limit_visibility_content)
  // console.log(slider_wrapper_length)

  let rest_of_content = no_of_content - limit_visibility_content;


  let limit_page_sliding = (no_of_content / limit_visibility_content)
  // console.log(limit_page_sliding)



  // Add event listeners for prev and next buttons


  nextBtn.addEventListener('click', () => {
    if (currentPage < limit_page_sliding) {

      if (rest_of_content < limit_visibility_content) {
        currentPosition -= (rest_of_content * 230)
      }
      else if (rest_of_content == limit_visibility_content) {
        currentPosition -= (228.5 * limit_visibility_content)
      }
      else {
        currentPosition -= (228.5 * limit_visibility_content)
      }

      movie_list_wrapper.style.transform = `translateX(${currentPosition}px)`;

      rest_of_content -= limit_visibility_content;

      if (rest_of_content <= 0) {
        rest_of_content += limit_visibility_content
      }
      currentPage++;
    }

  });



  prevBtn.addEventListener('click', () => {
    console.log("cPage", currentPage)

    if (currentPage > 1) {
      if (rest_of_content < limit_visibility_content) {
        currentPosition += (rest_of_content * 230)
      }
      else {
        currentPosition += (228.5 * limit_visibility_content)
      }
      movie_list_wrapper.style.transform = `translateX(${currentPosition}px)`
      // slider_wrapper_length += slider_wrapper_length
      currentPage--;
      if (currentPage == 1) {
        rest_of_content = no_of_content - (limit_visibility_content * 2)
      }
      rest_of_content += limit_visibility_content;

    }

  });

  $(item).ready(function(){

    $(prevBtn).hide()
    if(currentPage>=limit_page_sliding){
      $(nextBtn).hide()
    }
    else{
      $(nextBtn).show()
    }

    $(item).on("click",function(){
      if(currentPage==1){
        $(prevBtn).hide()
      }
      else{
        $(prevBtn).show()
      }

      if(currentPage>=limit_page_sliding){
        $(nextBtn).hide()
      }
      else{
        $(nextBtn).show()
      }


    })


  })








});

