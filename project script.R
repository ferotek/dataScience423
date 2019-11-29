gkmodel <- lm(Transfer.Values ~ GA+GA90+SoTA+Save+CS_A+CS+Penalties.saved
              +Punches+High.Claims+Catches+Goals.conceded+Clean.sheets+Errors.leading.to.goal, data = gk)
gkmodel1 <- lm(Transfer.Values ~1, data = gk)
summary(gkmodel)
stepgk <- stepAIC(gkmodel, direction = "backward")
gkmodel2 <- lm(Transfer.Values ~(CS_A + Penalties.saved + Punches + Clean.sheets)^2 , data = gk)
summary(gkmodel2)
gkmodel3 <- step(gkmodel, scope = . ~ .^2, direction = 'backward')
gkmodel4 <- stepAIC(gkmodel2, direction = "backward")
gkmodel5 <- lm(Transfer.Values ~(CS_A + Penalties.saved + Punches + Clean.sheets) , data = gk)
summary(gkmodel5)
gkmodel6 <- lm(Transfer.Values ~ CS_A + Punches + 
                 Clean.sheets + CS_A*Penalties.saved+ Age+ Age2, data = gk)
summary(gkmodel6)

gk$Age2 = gk$Age*gk$Age

train.control <- trainControl(method = "LOOCV")

gkmodel7 <- train(Transfer.Values ~ CS_A + Punches + 
                    Clean.sheets + CS_A*Penalties.saved+ Age+ Age2, data = gk, method = "lm",
               trControl = train.control)
print(gkmodel7)

train_control <- trainControl(method="LOOCV")
model <- train(Transfer.Values ~ CS_A + Penalties.saved + Clean.sheets + 
                 Punches, data = gk, trControl=train_control(method="LOOCV"))
print(model)

gkmodel8 <- stepAIC(gkmodel1,direction="forward", scope=list(upper=gkmodel,lower=gkmodel1))
print(gkmodel8)