from instapy import InstaPy



def main():

    tags = ["cars", "photo", "bmw", "fitness", "drift", "moto", "training", "food", "nature", "insta", "happy"]
    comments = ["Nice!", "Cool!", "This is unreal!!!"]


    session = InstaPy(username="_who.man_", password="enes51525354",  headless_browser=True, want_check_browser=False)
    # Запуск без графического интерфейса
    # session = InstaPy(username='test', password='test', headless_browser=True)

    # Вход
    session.login()
    # Устанавливаем ограничение дейтвий в день, час
    session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
    # Устанавливаем задержки для действий в секундах
    # session.set_action_delays(True, like=3, comment=5, follow=5, unfollow=5, story=10)
    # Отписываемся от людей, которые не подписались на нас
    # Устанавливаем ограничение на аккаунты у которых больше 8500 подписчиков
    session.set_relationship_bounds(enabled=True, max_followers=4000)
    # Подписываем на 50% аккаунтов, которым мы поставили лайк
    session.set_do_follow(True, percentage=50)
    # Оставляем комментарии на 50% аккаунтов, которым мы поставили лайк
    session.set_comments(comments)
    session.set_do_comment(True, percentage=50)

    # Отписываемся от аккаунтов на которые подписался бот, но они нас не подписались
    session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="all", style="FIFO", unfollow_after=(60 * 60 * 24), sleep_delay=501)
    # Ставим лайки по хештегам
    session.like_by_tags(tags, amount=2)
    # session.set_dont_like(["naked", "nsfw"])    

    session.end()


if __name__ == "__main__":
    main()
