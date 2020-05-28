from instapy import InstaPy



def main():

    tags = ["cars", "photo", "bmw", "fitness", "drift", "moto", "training", "food"]
    comments = ["Nice!", "Cool!", "This is unreal!!!"]

    session = InstaPy(username="+77029317645", password="enes51525354", want_check_browser=False)
    # Запуск без графического интерфейса
    #session = InstaPy(username='test', password='test', headless_browser=True)

    # Вход
    session.login()
    # Устанавливаем ограничение дейтвий в день, час
    session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
    # Устанавливаем задержки для действий в секундах
    session.set_action_delays(True, like=3, comment=5, follow=5, unfollow=5, story=10)
    # Отписываемся от людей, которые не подписались на нас
    session.unfollow_users(amount=50, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    # Устанавливаем ограничение на аккаунты у которых больше 8500 подписчиков
    session.set_relationship_bounds(enabled=True, max_followers=8500)

    # Ставим лайки по хештегам
    session.like_by_tags(tags, amount=2)
    # session.set_dont_like(["naked", "nsfw"])
    # Подписываем на 50% аккаунтов, которым мы поставили лайк
    session.set_do_follow(True, percentage=50)
    # Оставляем комментарии на 50% аккаунтов, которым мы поставили лайк
    session.set_comments(comments)
    session.set_do_comment(True, percentage=50)
    

    session.end()


if __name__ == "__main__":
    main()