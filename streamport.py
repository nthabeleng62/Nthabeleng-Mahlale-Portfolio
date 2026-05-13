import streamlit as st

st.set_page_config(page_title="Honours Portfolio", layout="wide")

# Sidebar navigation
page = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Projects", "Contact"]
)

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.title("Honours Year Portfolio")
    st.write("""
   This portfolio presents a curated overview of my Honours-year academic work in Risk Analysis, 
   with a focus on data-driven modelling, statistical analysis, and applied quantitative methods.

   Rather than showcasing full technical reports or complete codebases, this portfolio highlights:
   - The motivation behind each project  
   - The data and methods used  
   - Representative code snippets  
   - Key findings and conclusions  

   The aim is to demonstrate my analytical thinking, methodological choices, and ability to translate 
   quantitative analysis into meaningful insights. The projects span multiple modules, including 
   Big Data analytics, Financial Time Series modelling, Spatial Statistics, and Statistical Modelling.

   This portfolio also serves as a foundation for future academic and professional work in analytics, 
   risk modelling, research, and data-oriented roles.
    """)

# ---------------- ABOUT ME PAGE ----------------
elif page == "About Me":
    st.title("About Me")
    st.write("""
    My name is Nthabeleng Mahlale, and I am a quantitative and data-focused graduate with a strong 
    interest in analytics, statistical modelling, and structured problem-solving. I am particularly 
    motivated by using data-driven approaches to understand uncertainty, extract insights, and 
    support informed decision-making.

    I completed a Bachelor of Science in Actuarial Science followed by a Bachelor of Science Honours 
    in Risk Analysis at the University of the Free State. My academic training provided a solid 
    foundation in probability theory, statistics, financial mathematics, optimisation, and risk 
    modelling.

    During my Honours year, I developed advanced skills in applied statistical methods, machine 
    learning techniques, time series analysis, and spatial data analysis. I also strengthened my 
    ability to critically interpret results and communicate technical findings clearly.

    My interests include data analytics, predictive modelling, risk assessment, decision science, 
    and applied research. I enjoy breaking down complex problems into structured components and 
    developing models that reflect real-world behaviour.
             """)

# ---------------- PROJECTS PAGE ---------------- 
elif page == "Projects":
    st.title("Projects")

    st.write("""
    This section highlights selected coursework and projects completed during my Honours year.
    Each tab represents a different module, with emphasis on the project context, data used,
    representative code, and key outcomes rather than full technical implementations.
    """)

    # Create tabs for modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "Big Data",
        "Financial Time Series",
        "Spatial Statistics",
        "Statistical Modelling and Literature"
    ])

    # -------- TAB 1: BIG DATA --------
    with tab1:
        st.subheader("Big Data")

        st.markdown("### Introduction")
        st.write("""
        Traditional approaches to wine quality assessment rely heavily on human judgement, 
        making them subjective, resource-intensive, and vulnerable to bias. With the 
        increasing availability of physicochemical and categorical data, there is a 
        growing opportunity to apply data-driven methods that can evaluate wine quality 
        more objectively and consistently. This project explores the use of Quadratic Discriminant 
        Analysis (QDA) as a statistical classification technique capable of capturing complex, 
        non-linear relationships between chemical attributes and wine quality ratings.
        
        **Research Questions:**
        1. Can QDA effectively predict wine quality using physicochemical attributes?
        2. Which features (e.g., acidity, residual sugar, alcohol content, sulphates) play the most significant role in classifying wine quality?
        3. How accurate is the QDA model in differentiating between high- and low-quality wines?
        """)
        
        st.markdown("### Methodology")
        st.write("""
        This study employed a structured analytical framework to classify wine quality using 
        physicochemical properties. The dataset was first inspected and cleaned, with no missing values 
        detected, and all variables were standardised to ensure comparability. Wine quality scores were 
        grouped into three classes—low, medium, and high—and the data was split into training (70%) and 
        testing (30%) sets using stratified sampling to preserve class proportions. To improve adherence 
        to model assumptions, transformations such as Yeo–Johnson and Box–Cox were applied to reduce 
        skewness and approximate normality.
        
        Exploratory data analysis was conducted to examine variable distributions, correlations, and 
        relationships with wine quality. Highly correlated predictors were removed to mitigate 
        multicollinearity. Quadratic Discriminant Analysis (QDA) was then implemented, as it allows 
        class-specific covariance structures and non-linear decision boundaries suitable for the data. 
        Model parameters were estimated from the training set, and class membership was assigned using 
        posterior probabilities derived from Bayes’ theorem.
        
        Model stability and generalisation performance were assessed using 10-fold cross-validation. 
        Final evaluation was carried out on training, validation, and test sets using accuracy, Cohen’s 
        Kappa, precision, recall, F1-score, and AUC, with particular attention to class imbalance. All 
        analyses were performed in R, using established packages for modelling, validation, visualisation,
        and data manipulation.

""")
        
        st.markdown("### Data Used")
        st.write("""
        The data used contains 6,497 observations and 13 variables representing various 
        physicochemical and categorical attributes of wines. These variables include 
        measurements such as fixed acidity, volatile acidity, citric acid, residual sugar, 
        chlorides, sulphur dioxide levels (both free and total), density, pH, sulphates, 
        alcohol content, and a categorical variable distinguishing between red and white wines. 
        These features quantitatively capture the chemical composition and production characteristics 
        of the wines. The dataset also includes the wine quality ratings, originally on a scale from 
        0 to 10, which were later grouped into three categories for classification purposes: low 
        quality (ratings 3–4), medium quality (ratings 5–6), and high quality (ratings 7 and above).
        """)

        st.markdown("### Code Snippet")
        st.code('''
# ============================================================
# 6. Split into Training, Validation, and Test Sets (70-10-20)
# ============================================================
set.seed(123)
train_index <- createDataPartition(df_trans$quality_group, p = 0.7, list = FALSE)
train_data <- df_trans[train_index, ]
temp_data <- df_trans[-train_index, ]

set.seed(123)
val_index <- createDataPartition(temp_data$quality_group, p = 0.3333, list = FALSE)
validation_data <- temp_data[val_index, ]
test_data <- temp_data[-val_index, ]

# Convert quality_group to factor
train_data$quality_group <- as.factor(train_data$quality_group)
validation_data$quality_group <- as.factor(validation_data$quality_group)
test_data$quality_group <- as.factor(test_data$quality_group)

# ============================================================
# 7. Train QDA Model with 10-Fold Cross Validation
# ============================================================
ctrl <- trainControl(method = "cv", number = 10)

set.seed(123)
qda_cv_train <- train(
  quality_group ~ .,
  data = train_data[, c("quality_group", predictors_filtered, "is_red")],
  method = "qda",
  trControl = ctrl
)

print(qda_cv_train)
''', language="r")

        st.markdown("### Conclusion")
        st.write("""
        The study found that Quadratic Discriminant Analysis (QDA) achieved moderate classification
        performance, with an overall accuracy of approximately 78%, performing best on medium-quality 
        wines but struggling with low- and high-quality classes due to class imbalance. Alcohol content, 
        sulphates, and volatile acidity emerged as the most influential predictors of wine quality. 
        While data transformations and cross-validation improved model reliability, the effectiveness 
        of QDA was limited by unequal class distribution, skewness, correlated variables, and partially 
        unmet statistical assumptions. Overall, QDA proved to be a reasonable and interpretable approach, 
        though more robust methods could offer improved and more balanced classification performance.

        """)


    # -------- TAB 2: FINANCIAL TIME SERIES --------
    with tab2:
        st.subheader("Financial Time Series")

        st.markdown("### Introduction")
        st.write("""
        This projec, titled Comparison of SARIMA and LSTM Models for Hourly
        Ethereum Price Forecasting, focused on the analysis and forecasting of time series data, which 
        consists of observations collected sequentially over time, such as financial or environmental 
        data. Traditionally, time series have been modelled using ARIMA (Autoregressive Integrated Moving Average) 
        models and their variants, which are effective for small datasets and provide efficient forecasting. However, ARIMA models 
        are limited by their assumption of linearity and the subjective decisions required in model 
        selection.

        With the increasing availability of large and complex datasets, machine learning (ML) techniques have 
        emerged as powerful alternatives. Unlike traditional model-driven approaches, ML methods are data-driven, 
        capable of capturing non-linear patterns and complex relationships, often resulting in more accurate 
        predictions. This project explores the application of machine learning approaches such as Support Vector 
        Machines (SVMs), decision tree-based models, and deep learning to time series forecasting, with the goal 
        of improving predictive performance and extracting deeper insights from sequential data.
        
        **Research Questions:**
        1. How is the LSTM neural network architecture employed to model and forecast financial time series data?
        2. How is the ARIMA model utilized for the prediction of financial return series?
        3. What are the comparative performance characteristics of LSTM and ARIMA models in the context of financial time series forecasting?
        """)
        st.markdown("### Methodology")
        st.write("""
        This study analyses hourly Ethereum price data from 1 January 2020 to 10 September 2022, 
        including time, open, high, low, close prices, trading volume, and volume moving average. The 
        dataset was preprocessed by removing missing values. Open, high, low prices, volume, and volume 
        moving average were selected as independent variables, while the **closing price** served as the 
        target variable.
        
        Two forecasting models were implemented and compared. An ARIMA model was fitted to the closing 
        price series, with model order selection guided by ACF, PACF, and EACF analyses, resulting in an 
        ARIMA(0,1,2) specification. Model adequacy was assessed using information criteria and residual 
        diagnostics to confirm stationarity and independence. In parallel, an LSTM model was developed by
        scaling the data using min–max normalization and constructing input sequences with a 20-step 
        sliding window. The network comprised a single LSTM layer with 50 units and a dense output layer,
        trained using the Adam optimizer and mean squared error loss over 20 epochs with a batch size of 
        32.
        
        Model performance was evaluated by comparing ARIMA and LSTM forecasts using MSE, RMSE, and MASE, 
        allowing for an assessment of predictive accuracy across both statistical and deep learning 
        approaches.
                             """)

        st.markdown("### Data Used")
        st.write("""
        Ethereum is the second most traded cryptocurrency after Bitcoin, holding about 9–11% of the 
        market capitalization, compared to Bitcoin’s 58–60%. The dataset used in this project was 
        extracted from FTX via TradingView (Kaggle.com, accessed 7 May 2025) and consists of Perpetual 
        Futures contracts from 1 January 2020 to 10 September 2022, comprising 23,596 hourly data points 
        after removing initial entries with missing values.

        The dataset includes the following variables: time (Unix timestamp), open, high, low, close prices, 
        trading volume, and the 20-hour moving average of volume (volume MA). These variables capture the price 
        and trading activity each hour, providing a reliable foundation for analysis and predictive modelling of 
        Ethereum price movements.
        """)

        st.markdown("### Code Snippet")
        st.code("""
##choose model.arima 
#model_arima <- arima(Closemodel_arima <- arima(Close, order = c(0, 0, 2)))
fitted_arima <- fitted(model_arima)

# Scale ARIMA-fitted values like the rest
scaled_close <- (Close - min(Close)) / (max(Close) - min(Close))
scaled_fitted_arima <- (fitted_arima - min(Close)) / (max(Close) - min(Close))

# Align ARIMA to match LSTM output length
aligned_arima <- scaled_fitted_arima[(sequence_length + 1):length(scaled_fitted_arima)]
###SARIMA vs the Actual 

plot(y_aligned, type = "l", col = "blue", lwd = 2, 
     main = "Actual vs LSTM vs ARIMA (Aligned & Scaled)", 
     xlab = "Index", ylab = "Scaled Value")
lines(aligned_arima, col = "darkgreen", lwd = 1)
legend("topleft", legend = c("Actual", "ARIMA Fitted"), 
       col = c("blue", "darkgreen"), 
       lty = 1, pch = c(NA, NA), lwd = c(2, 1))


#############################################################################


# Plot Actual vs LSTM vs ARIMA
plot(y_aligned, type = "l", col = "blue", lwd = 2, 
     main = "Actual vs LSTM vs ARIMA (Aligned & Scaled)", 
     xlab = "Index", ylab = "Scaled Value")

lines(predicted_lstm_aligned, col = "pink", type = "b", pch = 1, cex = 0.3)
lines(aligned_arima, col = "darkgreen", lwd = 1)

legend("topleft", legend = c("Actual", "LSTM Predicted", "ARIMA Fitted"), 
       col = c("blue", "pink", "darkgreen"), 
       lty = 1, pch = c(NA, 1, NA), lwd = c(2, 1, 1))

""", language="r")

        st.markdown("### Conclusion")
        st.write("""
       The conclusion was that Ethereum closing prices can be predicted very well using 
       machine learning, specifically through LSTM modeling. The LSTM model captured the overall trend 
       of the data effectively but may struggle with capturing the full variability, which might indicate 
       some overfitting. Overall, based on most performance metrics, the LSTM model outperformed the ARIMA model in forecasting accuracy for the Ethereum hourly closing prices
        """)

    # -------- TAB 3: SPATIAL STATISTICS --------
    with tab3:
        st.subheader("Spatial Statistics")

        st.markdown("### Introduction")
        st.write("""
        This project examined the spatial distribution of schools in Bloemfontein to determine whether 
        they are clustered, dispersed, or randomly distributed. It explores differences by school type, 
        identifies areas with inadequate access, and considers how current patterns reflect historical 
        apartheid-era planning. Using rigorous spatial statistical analysis, the study aims to provide 
        evidence-based insights to guide equitable educational planning and address persistent access 
        inequalities.
        
        """)
        
        st.markdown("### Methodology")
        st.write("""
        This study applies Point Pattern Analysis (PPA) to examine the spatial distribution of schools 
        and determine whether their locations exhibit clustering, randomness, or dispersion. The analysis
        is conducted using R and ArcGIS, enabling both statistical testing and spatial visualisation. 
        Multiple complementary techniques are employed to capture spatial patterns at different scales 
        and levels of detail.

        The methods include Average Nearest Neighbour (ANN) to assess local clustering or dispersion 
        based on inter-point distances, **Global Moran’s I** to measure spatial autocorrelation, and 
        the Quadrat Count method to evaluate distribution patterns using grid-based counts supported by 
        chi-square tests and variance-to-mean ratios. Ripley’s K-function is used to investigate 
        clustering or dispersion across varying spatial distances, allowing for multi-scale pattern 
        detection. In addition, Kernel Density Estimation is applied to identify and visualise 
        concentration hotspots, while Voronoi maps are used to define school catchment areas and 
        highlight spatial inequalities in accessibility.

        Together, these methods provide a robust and comprehensive framework for analysing school 
        distribution by combining statistical validation, multi-scale assessment, and intuitive 
        visualisation, offering valuable insights for spatial planning and policy development.
                             """)

        st.markdown("### Data Used")
        st.write("""
         The dataset is consisting of 125 schools in Bloemfontein and their locations coordinates, made 
         up of primary schools, secondary school and combined schools (which consists of both primary 
        and secondary grades). It is then used in this paper to comprises comprehensive spatial and 
        attribute data of schools in Bloemfontein. It was collected from the Free State Provincial 
        Department of Education and Google Maps, forming a near-census of schools within the city. 
        """)

        st.markdown("### Code Snippet")
        st.code("""
# SECTION 5: ANALYSIS OF COMBINED SCHOOLS
# ============================================================================

# --- 5.1 Data Import and Preparation ---
combined <- read_excel("C:/Users/2018345104/Downloads/COMBINED SCHOOLS.xlsx")
View(combined)

# Rename columns
colnames(combined)[colnames(combined) == "Longitude"] <- "X"
colnames(combined)[colnames(combined) == "Latitude"]  <- "Y"

# Convert to spatial object
combined_school <- st_as_sf(combined, coords = c("X", "Y"), crs = 4326)

# Reproject
combined_sch <- st_transform(combined_school, 32735)

# Create window
bbox <- st_bbox(combined_sch)
window <- owin(xrange = c(bbox["xmin"], bbox["xmax"]),
               yrange = c(bbox["ymin"], bbox["ymax"]))

# Convert to ppp
combined_ppp <- as.ppp(st_coordinates(combined_sch), W = window)

# --- 5.2 Nearest Neighbour Analysis ---
mean_nn_dist <- mean(nndist(combined_ppp))
lambda <- intensity(combined_ppp)
expected_nn_dist <- 1 / (2 * sqrt(lambda))
R <- mean_nn_dist / expected_nn_dist

cat("=== COMBINED SCHOOLS ===\n")
cat("Observed Mean NN distance:", mean_nn_dist, "meters\n")
cat("Expected NN distance (CSR):", expected_nn_dist, "meters\n")
cat("Clark-Evans R:", R, "\n")

if(R < 1) {
  cat("→ Combined schools are CLUSTERED.\n")
} else if(R > 1) {
  cat("→ Combined schools are REGULARLY DISPERSED.\n")
} else {
  cat("→ Combined schools follow CSR.\n")
}

plot(combined_ppp, main = "Combined Schools - Point Pattern")

# --- 5.3 Quadrat Count Analysis ---
Q_3 <- quadratcount(combined_ppp, nx = 3, ny = 3)
plot(Q_3, main = "Quadrat Count (3x3) for Combined Schools")
plot(combined_ppp, add = TRUE, pch = 16, col = "hotpink")

Q_5 <- quadratcount(combined_ppp, nx = 5, ny = 5)
plot(Q_5, main = "Quadrat Count (5x5) for Combined Schools")
plot(combined_ppp, add = TRUE, pch = 16, col = "hotpink")

Q_10 <- quadratcount(combined_ppp, nx = 10, ny = 10)
plot(Q_10, main = "Quadrat Count (10x10) for Combined Schools")
plot(combined_ppp, add = TRUE, pch = 16, col = "hotpink")

# Chi-square test
Q_test <- quadrat.test(combined_ppp, nx = 3, ny = 3)
print(Q_test)

# VMR
counts <- as.vector(Q_10)
VMR <- var(counts) / mean(counts)
cat("Combined Schools VMR:", VMR, "\n")

# --- 5.4 Ripley's K-function ---
K_combined <- Kest(combined_ppp)
plot(K_combined, main = "Ripley's K-function for Combined Schools")

# --- 5.5 Kernel Density ---
dens_combined <- density(combined_ppp, sigma = bw.diggle)
plot(dens_combined, main = "Kernel Density of Combined Schools")
plot(combined_ppp, add = TRUE, pch = 16, cex = 0.5, col = "yellow")


""", language="r")

        st.markdown("### Conclusion")
        st.write("""
       Overall, the spatial analyses consistently indicate that schools are not randomly distributed 
       but are predominantly **clustered**, particularly within central urban areas. Nearest Neighbour, 
       Moran’s I, Quadrat Count, and Ripley’s K analyses all confirm significant clustering across most 
       school types, with especially strong clustering observed for primary schools and for schools 
       overall. Secondary and combined schools show weaker clustering or near-random patterns in some 
       tests, but still exhibit clustering at multiple spatial scales. Kernel density and Voronoi 
       analyses further reveal pronounced **urban hotspots** and reduced access in peripheral areas, 
       highlighting clear spatial inequalities in school distribution and accessibility.

        """)

    # -------- TAB 4: STATISTICAL MODELLING AND LITERATURE --------
    with tab4:
        st.subheader("Statistical Modelling and Literature")

        st.markdown("### Introduction")
        st.write("""
        Cryptocurrencies have emerged as a distinct asset class, offering diversification opportunities 
        and enabling decentralized financial systems that facilitate fast, secure, and low-cost 
        transactions outside traditional banking infrastructures. As cryptocurrency markets continue to 
        grow, effective portfolio and risk management have become increasingly important for informed 
        trading and investment decisions. This study focuses on cryptocurrency trading by analysing 
        potential profits and losses through return behaviour, market trends, trading volumes, and 
        market capitalisation, with particular attention given to the top three cryptocurrencies by 
        market value.

        Financial return data, including cryptocurrency returns, are well known to exhibit heavy tails, 
        skewness, and high kurtosis, making traditional modelling approaches inadequate for accurate risk
        assessment. To address this, the study employs heavy-tailed statistical distributions that better
        capture extreme movements in returns and provide a more realistic framework for risk modelling. 
        By accounting for these characteristics, the paper aims to improve the understanding of risk 
        dynamics in cryptocurrency markets and support more robust investment and risk management 
        strategies.

        """)
        
        st.markdown("### Methodology")
        st.write("""
        This study employs an extensive statistical modelling approach to analyse the return behaviour 
        of cryptocurrencies, focusing on their volatile, asymmetric, and non-normal characteristics. 
        Returns for **Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP)** are separated into gains and 
        losses, and **22 statistical distributions** are fitted to each return type. Model performance 
        is evaluated using six goodness-of-fit tests alongside key risk measures, namely Value at Risk 
        (VaR) and Expected Shortfall (ES), which are also compared to empirical estimates across multiple
        confidence levels.

        To identify the most suitable models, a **ranking system** is applied that integrates both 
        statistical fit and risk performance. Unlike earlier studies, this methodology evaluates risk 
        measures for all fitted distributions rather than relying solely on information criteria such as 
        AIC or BIC. The framework culminates in a dual-objective selection process to determine the 
        best-performing distribution for each cryptocurrency and return type, providing a comprehensive 
        and rigorous approach to cryptocurrency risk modelling.
                             """)

        st.markdown("### Data Used")
        st.write("""
        The data used in this study consists of cryptocurrency market information drawn from publicly 
        available sources, with a focus on assets operating on blockchain-based, decentralized networks. 
        The analysis relies on **market capitalization** as the primary criterion for selecting 
        cryptocurrencies, where market capitalization is calculated as the product of the asset’s 
        reference price and its circulating supply. This measure is widely used to rank cryptoassets and 
        to reflect their relative size and market importance.

        At the time of data extraction in early February 2025, the cryptocurrency market comprised 
        several thousand assets, with total market capitalization exceeding USD 3 trillion. Based on 
        market cap rankings from CoinMarketCap, the **top three cryptocurrencies—Bitcoin (BTC), Ethereum 
        (ETH), and Ripple (XRP)**—were selected for analysis. These assets were chosen due to their 
        large market presence, high trading activity, and economic relevance. The dataset captures the 
        inherently volatile nature of cryptocurrency prices and market capitalization, making it 
        suitable for analysing return behaviour, risk characteristics, and market dynamics.

        """)

        st.markdown("### Code Snippet")
        st.code("""
#######WEIBULL

#Parameter Estimates and NLL for LOSSES
btclosses_weib = fitdist(btclosses, "weibull",  method = "mle")
summary(btclosses_weib)
shape.loss_weib = btclosses_weib$estimate[1]
scale.loss_weib = btclosses_weib$estimate[2]

#Goodness of fit tests (excluding NLL)
gofstat(btclosses_weib, fitnames = "Fitting Weibull to BTC losses")

hist(btclosses, breaks = 40, freq = F, main = "", xlab = expression('BTC'[losses]))
lines(density(rweibull(100000,shape.loss_weib, scale.loss_weib)))
qqplot(btclosses, rweibull(100000,shape.loss_weib, scale.loss_weib), main = "",
       xlab = expression('BTC'[losses]), ylab = expression('QQ'[Weibull]))
abline(0,1)


#Parameter Estimates and NLL for GAINS
btcgains_weib = fitdist(btcgains, "weibull", method = "mle")
summary(btcgains_weib)
shape.gain_weib = btcgains_weib$estimate[1]
scale.gain_weib = btcgains_weib$estimate[2]

hist(btcgains, breaks = 50, freq = F, main = "", xlab = expression('BTC'[gains]))
lines(density(rweibull(1000000,shape.gain_weib, scale.gain_weib)))
qqplot(btcgains, rweibull(1000000,shape.gain_weib, scale.gain_weib), main = "",
       xlab = expression('BTC'[gains]), ylab = expression('QQ'[Weibull]))
abline(0,1)

#Goodness of fit tests (excluding NLL)
gofstat(btcgains_weib, fitnames = "Fitting Weibull to BTC gains")


#######BURR

#Parameter Estimates and NLL for LOSSES
detach("package:ReIns", unload = TRUE)

btclosses_burr = fitdist(btclosses, "burr", start = list(shape1 = 57, scale = 1.5, shape2 = 1), method = "mle")
summary(btclosses_burr)
shape1.loss_burr = btclosses_burr$estimate[1]
shape2.loss_burr = btclosses_burr$estimate[3]
scale.loss_burr = btclosses_burr$estimate[2]

#Goodness of fit tests (excluding NLL)
gofstat(btclosses_burr, fitnames = "Fitting Burr to BTC losses")

hist(btclosses, breaks = 40, freq = F, main = "", xlab = expression('BTC'[losses]))
lines(density(rburr(100000,shape1.loss_burr, shape2.loss_burr, scale = scale.loss_burr)))
qqplot(btclosses, rburr(100000,shape1.loss_burr, shape2.loss_burr, scale = scale.loss_burr), main = "",
       xlab = expression('BTC'[losses]), ylab = expression('QQ'[Burr]))
abline(0,1)


#Parameter Estimates and NLL for GAINS
btcgains_burr = fitdist(btcgains, "burr", start = list(shape1 = 2548, scale = 71, shape2 = 1),method = "mle")
summary(btcgains_burr)
shape1.gain_burr = btcgains_burr$estimate[1]
shape2.gain_burr = btcgains_burr$estimate[3]
scale.gain_burr = btcgains_burr$estimate[2]

hist(btcgains, breaks = 35, freq = F, main = "", xlab = expression('BTC'[gains]))
lines(density(rburr(100000,shape1.gain_burr, shape2.gain_burr, scale = scale.gain_burr)))
qqplot(btcgains, rburr(100000,shape1.gain_burr, shape2.gain_burr, scale = scale.gain_burr), main = "",
       xlab = expression('BTC'[gains]), ylab = expression('QQ'[Burr]))
abline(0,1)

#Goodness of fit tests (excluding NLL)
gofstat(btcgains_burr, fitnames = "Fitting Burr to BTC gains")

""", language="r")

        st.markdown("### Conclusion")
        st.write("""
        In summary, this study provides a comprehensive and innovative analysis of cryptocurrency return 
        behaviour, offering meaningful contributions to both theory and practice. By examining multiple 
        return types across three major digital assets and evaluating them using a wide range of 
        carefully selected statistical distributions, the research extends existing work in the field 
        while addressing key limitations in prior studies. The integration of statistical goodness-of-fit
        measures with financially relevant performance metrics, together with the adaptation of classical
        actuarial models to a contemporary cryptocurrency setting, results in a balanced and practical 
        risk-modelling framework. Overall, the findings offer valuable insights and applicable tools for 
        researchers and financial practitioners, supporting more informed risk assessment in digital 
        asset markets.

        """)

# ---------------- CONTACT PAGE ----------------
elif page == "Contact":
    st.title("Contact")
    st.write("Email: nthabelengmahlale@gmail.com")
    st.markdown(
        "LinkedIn: [linkedin.com/in/nthabelengmahlale](https://www.linkedin.com/in/nthabelengmahlale)"
    )