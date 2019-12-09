<?php
$json_string = file_get_contents('movie_ranking.json');
$R=json_decode($json_string,true);
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>One click MOVIE</title>

    <!-- Custom fonts for this theme -->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- Theme CSS -->
    <link href="css/freelancer.min.css" rel="stylesheet">
    <style>
        .card-img-top{
            height: 350px;!important;
        }
        .card-footer{
            height: 200px;!important;
        }
        .sbox{
            -webkit-appearance: none; /* 네이티브 외형 감추기 */
            -moz-appearance: none;
            appearance: none;
            background: url(img/arrow.png) no-repeat 95% 50%;


        }
       .sbox::-ms-expand { display: none; }
    </style>
</head>

<body id="page-top">

<!-- Navigation -->
<nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
    <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">One click MOVIE</a>
        <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item mx-0 mx-lg-1">
                    <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#contact">영화 랭킹</a>
                </li>
                <li class="nav-item mx-0 mx-lg-1">
                    <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">상영 정보</a>
                </li>
                <li class="nav-item mx-0 mx-lg-1">
                    <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">영화 핫이슈</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- Jumbotron Header -->
<header class="jumbotron my-4" style="padding-top: 7%;">

    <h1 class="display-3" style="font-size:60px; font-weight: bold;">모든 영화관을 한 눈에!</h1>
    <p class="lead" style="font-weight: bold;">그 동안 영화시간을 찾아 여기저기 헤매셨던 당신에게, 편리한 서비스를 제공합니다.<br>모든 영화관의 상영정보를 바로 여기, 한 곳에서!</p>
    <a href="#portfolio" class="btn btn-primary btn-lg">상영 정보</a>

</header>

<!-- Contact Section -->
<section class="page-section" id="contact" style="margin-left: 25%;margin-right: 25%;">
    <!-- 영화 순위 출력 부분 -->
    <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
            <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
    </div>
    <center><div>
            <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">영화 랭킹</h2>
            <p>매일 9:00AM 업데이트</p>
            <br/>
        </div></center>
    <div class="row text-center">
        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/1.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">1 &nbsp;&nbsp;
                        <?php
                        print $R[1]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[1]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[1]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[1]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/2.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">2 &nbsp;&nbsp;
                        <?php
                        print $R[2]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[2]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[2]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[2]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/3.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">3 &nbsp;&nbsp;
                        <?php
                        print $R[3]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[3]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[3]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[3]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/4.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">4 &nbsp;&nbsp;
                        <?php
                        print $R[4]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[4]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[4]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[4]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/5.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">5 &nbsp;&nbsp;
                        <?php
                        print $R[5]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[5]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[5]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[5]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/6.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">6 &nbsp;&nbsp;
                        <?php
                        print $R[6]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[6]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[6]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[6]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/7.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">7 &nbsp;&nbsp;
                        <?php
                        print $R[7]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[7]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[7]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[7]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6 mb-4">
            <div class="card h-100">
                <img class="card-img-top" src="poster/8.jpg" alt="">
                <div class="card-footer">
                    <h5 class="card-text">8 &nbsp;&nbsp;
                        <?php
                        print $R[8]['title'];
                        print '<br/>';
                        ?>
                    </h5>
                    <p class="card-text">개봉 :
                        <?php
                        print $R[8]['release'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">일간 :
                        <?php
                        print $R[8]['Today'];
                        print '<br/>';
                        ?>
                    </p>
                    <p class="card-text">누적 :
                        <?php
                        print $R[8]['accumulate'];
                        print '<br/>';
                        ?>
                    </p>
                </div>
            </div>
        </div>
    </div>
    <!-- /.row -->
</section>

<!-- Portfolio Section -->
<section class="page-section portfolio" id="portfolio">
    <div class="container">
        <!-- Icon Divider -->
        <div class="divider-custom">
            <div class="divider-custom-line"></div>
            <div class="divider-custom-icon">
                <i class="fas fa-star"></i>
            </div>
            <div class="divider-custom-line"></div>
        </div>
        <center><div>
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">영화 시간표</h2>
                <p>원하는 영화의 상영 정보를 한 번에 확인하세요!</p>
                <br/>
            </div></center>
            <div>
                <form method="post" action="action_popup.php" target="if1">
                    <select name="mname" id="selectBox" class="sbox" style="width: 200px; height: 50px;"">
                    <option value="">영화 선택</option>
                <?php
                include "dbconfig.php";
                $sql = "SELECT DISTINCT * FROM store";
                $result = $conn->query($sql);
                echo "<option>";
                if($result->num_rows >0){
                    while($row=$result->fetch_assoc()) {
                        echo $row["Stno"]."<br><option/>";
                    }
                }else{
                    echo "0 result";
                }
                $conn->close();
                ?><select/>

                &nbsp;&nbsp;&nbsp;
                        <select name="lname" class="sbox" style="width: 100px; height: 50px;">
                            <option>청주시</option>
                            <option>청주시</option>
                            <option>청주시</option>
                            <option>청주시</option>
                        </select>
                    &nbsp;&nbsp;&nbsp;

                        <button type="submit" class="btn btn-primary btn-xl" id="selectButton">선택</button>
                        <form/>
                        <br><br><br>
        </div>
            <iframe name="if1">
            </iframe>
            <div/>

</section>
<hr class="ht-line">
<!-- About Section -->
<section class="page-section bg-primary text-white mb-0" id="about" style="background-color: #ffffff !important;">
    <div class="container">
        <!-- Icon Divider -->

        <div class="divider-custom divider-light" style="color: #1ABC9C !important;">
            <div class="divider-custom-line" style="color: #1ABC9C !important;"></div>
            <div class="divider-custom-icon" style="color: #1ABC9C !important;">
                <i class="fas fa-star" style="color: #1ABC9C !important;"></i>
            </div>
            <div class="divider-custom-line" style="color: #1ABC9C !important;"></div>
        </div>
        <!-- About Section Heading -->
        <h2 class="page-section-heading text-center text-uppercase text-white" style="color: #1ABC9C !important;">영화 핫이슈</h2>
        <br/>
        <center><p style="color: black !important;">이미지를 클릭하면 다음 영화 매거진으로 이동합니다!</p>
        </center>

        <!-- About Section Content -->
        <div class="row" style="color: #1ABC9C !important;">
        </div>
        <div id="wc" class="text-center mt-4">
            <a href="https://movie.daum.net/magazine/new"><img width="1100" height="550" src="img/wordcloud.png"></a>
        </div>

    </div>
</section>


<!-- Footer -->
<footer class="footer text-center">
    <div class="container">
        <div class="row">

            <!-- Footer Location -->
            <div class="col-lg-4 mb-5 mb-lg-0">
                <h4 class="text-uppercase mb-4">Location</h4>
                <p class="lead mb-0">충북 청주시 서원구 충대로1
                    <br>충북대학교 소프트웨어학과 (S4-1)</p>
            </div>


            <div class="col-lg-4 mb-5 mb-lg-0">
            </div>
            <!-- Footer link -->
            <div class="col-lg-4 mb-5 mb-lg-0">
                <h4 class="text-uppercase mb-4">CONTACT</h4>
                <p class="lead mb-0">jinoh
                    <br>Yujeong<br/>Ahyun</p>
            </div>
        </div>
    </div>
</footer>

<!-- Copyright Section -->
<section class="copyright py-4 text-center text-white">
    <div class="container">
        <small>Copyright &copy; Jinoh&nbsp;&nbsp;&nbsp;Yujeong&nbsp;&nbsp;&nbsp;Ahyun</small>
    </div>
</section>

<!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
<div class="scroll-to-top d-lg-none position-fixed ">
    <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top">
        <i class="fa fa-chevron-up"></i>
    </a>
</div>


<!-- Bootstrap core JavaScript -->
<script src="vendor/jquery/jquery.min.js"></script>
<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Plugin JavaScript -->
<script src="vendor/jquery-easing/jquery.easing.min.js"></script>

<!-- Contact Form JavaScript -->
<script src="js/jqBootstrapValidation.js"></script>
<script src="js/contact_me.js"></script>

<!-- Custom scripts for this template -->
<script src="js/freelancer.min.js"></script>

</body>

</html>
