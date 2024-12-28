from src.selenium.twitter_scraper import scrape_trending_topics

def test_scrape_trending_topics():
    result = scrape_trending_topics()
    assert len(result["trends"]) == 5
    assert "datetime" in result
    assert "ip_address" in result
