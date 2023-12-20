from business_rule_engine import RuleParser

def ruleBasedAnswer(math, we, ns, fl, ss, hum, eng, sci, health):
    params = {
        "Math": math,
        "Written_expression": we,
        "Natural_sciences": ns,
        "Foreign_language": fl,
        "Social_sciences": ss,
        "Humanities": hum,
        "Engineering": eng,
        "Sciences": sci,
        "Health": health
    }

    def defResult(str):
        global result
        result = str


    rules = """
    rule "aced student"
    when
        AND(Math > 80, Written_expression > 80, Natural_sciences > 80,
        Foreign_language > 80, Social_sciences > 80)
    then
        defResult("You can study your highest preference career!")
    end

    rule "Eng or Sci"
    when
        AND(Math > 80, 
        Natural_sciences > 80)
    then
        defResult("You can study engineering or science!")
    end

    rule "Hum or Health"
    when
        AND(OR(Engineering > 7, Sciences > 7), Math < 60)
    then
        defResult("You can study Humanities or Health!")
    end

    rule "Hum"
    when
        AND(Natural_sciences < 60, Health > 7)
    then
        defResult("You can study Humanities!")
    end

    """

    parser = RuleParser()
    parser.register_function(defResult)
    parser.parsestr(rules)
    parser.execute(params)
    return result

