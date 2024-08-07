import discord

def setup_help_command(bot):
    @bot.tree.command(name='도움말')
    async def help_command(interaction: discord.Interaction):
        """🍊 규리를 어떻게 사용하는 지 도움을 드려요!!"""
        help_message = (
            "**규리설명서** 🍊\n\n"
            "안녕하세요! 저는 규리예요! 🍊\n\n"
            "여기 제가 할 수 있는 일들이에요. 사용 예시도 함께 알려드릴게요!\n\n"
            "**🌟 일반 명령어 🌟**\n"
            "• **`/인사`** - 규리가 반갑게 인사해요!\n"
            "  *사용 예시*: `/인사`\n\n"
            "• **`/도움말`** - 규리를 어떻게 사용하는지 도움을 드려요!\n"
            "  *사용 예시*: `/도움말`\n\n"
            "**🔧 유틸리티 명령어 🔧**\n"
            "• **`/굴려`** - 규리가 주사위를 굴려요! (1부터 100 사이의 숫자를 무작위로 선택)\n"
            "  *사용 예시*: `/굴려`\n\n"
            "• **`/짤`** - 채팅방에 짤을 소환해요! (짤 목록에서 선택)\n"
            "  *사용 예시*: `/짤`\n\n"
            "• **`/날씨`** - 규리가 날씨 정보를 제공해드려요! (오늘과 미래의 날씨)\n"
            "  *사용 예시*: `/날씨`\n"
            "  *자동 공지 시간*: 매일 아침 7시에 오늘의 날씨 정보를 알려드립니다.\n\n"
            "**🚍 교통 관련 명령어 🚍**\n"
            "• **`/버스숙소`** - 숙소에서 교육장으로 가는 실시간 버스 정보를 알려드려요.\n"
            "  *사용 예시*: `/버스숙소`\n"
            "  *자동 공지 시간*: 매일 07:30-08:30, 5분마다 교육장으로 가는 버스 정보를 알려드립니다.\n\n"
            "• **`/버스교육장`** - 교육장에서 숙소로 가는 실시간 버스 정보를 알려드려요.\n"
            "  *사용 예시*: `/버스교육장`\n"
            "  *자동 공지 시간*: 매일 21:30-23:00, 5분마다 숙소로 향하는 버스 정보를 알려드립니다.\n\n"
            "**👥 모임 관리 명령어 👥**\n"
            "• **`/모임`** - 규리가 소모임을 위한 음성 채널을 만들어드려요! (모임 이름과 초대 메시지 필요)\n"
            "  *사용 예시*: `/모임 name:스터디 invite_message:스터디 모임에 초대합니다!`\n\n"
            "• **`/모임제거`** - 여러분이 만든 모임을 규리가 치워드릴게요!\n"
            "  *사용 예시*: `/모임제거`\n\n"
            "**🚖 택시 모집 명령어 🚖**\n"
            "• **`/택시`** - 규리가 택시를 모집합니다. 함께 가요! (목적지, 출발 시간, 모집 인원 필요)\n"
            "  *사용 예시*: `/택시 목적지:교육장 시간:08:00 모집인원:3`\n\n"
            "• **`/택시조회`** - 생성된 택시 모집을 조회해요.\n"
            "  *사용 예시*: `/택시조회`\n\n"
            "• **`/택시참여`** - 내가 참여한 택시 모집을 조회해요.\n"
            "  *사용 예시*: `/택시참여`\n\n"
            "• **`/택시삭제`** - 내가 만든 택시 모집을 삭제해요.\n"
            "  *사용 예시*: `/택시삭제`\n\n"
            "**🗳️ 투표 명령어 🗳️**\n"
            "• **`/투표`** - 투표를 생성합니다. (제목, 옵션들, 복수 응답 허용 여부, 투표 시간 필요)\n"
            "  *사용 예시*: `/투표 title:점심 메뉴 투표 options:한식, 중식, 일식 allow_multiple_votes:False time:60`\n\n"
            "• **`/투표제거`** - 활성화된 투표 목록을 보여주고, 선택한 투표를 삭제해요.\n"
            "  *사용 예시*: `/투표제거`\n\n"
            "• **`/투표수정`** - 기존 투표를 수정해요.\n"
            "  *사용 예시*: `/투표수정 title:점심 메뉴 투표 options:양식, 멕시칸 allow_multiple_votes:True time:120`\n\n"
            "**📅 데일리 스레드 명령어 📅**\n"
            "• **`/데일리`** - 규리가 데일리 스레드를 만들게요! (시작 or 정지, 텍스트 채널 필요)\n"
            "  *사용 예시*: `/데일리 start_or_stop:시작 channel:일반`\n\n"
            "• **`/데일리_태그`** - 알림에 맨션할 사람을 추가해요! (추가 or 삭제, 사용자들 필요)\n"
            "  *사용 예시*: `/데일리_태그 add_or_delete:추가 user:@사용자1 user1:@사용자2`\n\n"
            "제가 도와드릴 수 있는 부분이 있다면 언제든지 말씀해주세요! 🍊"
        )
        await interaction.response.send_message(help_message, ephemeral=True)
