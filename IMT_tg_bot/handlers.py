from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import keyboards as kb

router = Router()


class IMT(StatesGroup):
    massa = State()
    height = State()


@router.message(F.text == "Вычислить ИМТ")
async def imt(message: Message, state: FSMContext):
    await state.set_state(IMT.massa)
    await message.answer("Введите ваш вес")


@router.message(IMT.massa)
async def massa(message: Message, state: FSMContext):
    try:
        await state.update_data(massa=int(message.text))
        await state.set_state(IMT.height)
        await message.answer("Введите ваш рост")
    except ValueError:
        await message.answer("Ваш вес пожалуйста :D")
        await state.set_state(IMT.massa)


@router.message(IMT.height)
async def heihgt(message: Message, state: FSMContext):
    try:
        await state.update_data(height=int(message.text))
        data = await state.get_data()
        heig = data["height"] / 100
        imt_otvet = round(data["massa"] / (heig * heig), 1)
        await message.answer(f"Ваш ИМТ равен: {imt_otvet}")
        await message.answer("У вас:")

        if imt_otvet < 16:
            await message.answer("Значительный дефицит массы")
        elif imt_otvet <= 18.5:
            await message.answer("Дефицит массы тела")
        elif imt_otvet <= 25:
            await message.answer("Норма")
        elif imt_otvet <= 30:
            await message.answer("Лишний вес")
        elif imt_otvet <= 35:
            await message.answer("Ожирение 1-й степени")
        elif imt_otvet <= 40:
            await message.answer("Ожирение 2-й степени")
        elif imt_otvet > 40:
            await message.answer("Ожирение 3-й степени")

        await state.clear()
    except ValueError:
        await message.answer("Ваш рост пожалуйста :)")
        await state.set_state(IMT.height)


@router.message(F.text == "Узнать что такое ИМТ")
async def hello(message: Message):
    await message.answer("Величина, позволяющая оценить степень соответствия массы человека"
                         " и его роста и тем самым косвенно судить о том, является ли масса"
                         " недостаточной, нормальной или избыточной.")


@router.message(F.text == "Категории ИМТ")
async def imt_pic(message: Message):
    photo = FSInputFile("IMT_picture.jpg")
    await message.answer_photo(photo=photo)


@router.message(F.text == "Упражнения для тренировки")
async def trening(message: Message):
    await message.answer("Какое именно упражнение?", reply_markup=kb.trening)


class Trening:
    @staticmethod
    @router.message(F.text == "Наклоны головой")
    async def naklon_golovoi(message: Message):
        await message.answer("Наклоны головой - вперед, назад, влево, вправо 20-30 раз (расслабляет мышцы шеи)")
        gif = FSInputFile("upr/Naklony_golovy_na_stule.gif")
        await message.answer_video(video=gif)

    @staticmethod
    @router.message(F.text == "Махи руками")
    async def maxi_rukami(message: Message):
        await message.answer("Махи руками вдоль тела - 10-12 раз (помогают «встряхнуться», "
                             "разминают руки, плечи и спину, дают энергию и бодрость)")
        gif = FSInputFile("upr/Mahi_rukami_zaryadka.gif")
        await message.answer_video(video=gif)

    @staticmethod
    @router.message(F.text == "Наклоны вдоль тела")
    async def nakloni_tela(message: Message):
        await message.answer("    Наклоны вдоль тела - влево и вправо 10-12 раз "
                             "(помогает растянуть мышцы спины и избавиться от проблем с позвоночником)")
        gif = FSInputFile("upr/Naklony_v_storonu_dlya_spiny.gif")
        await message.answer_video(video=gif)

    @staticmethod
    @router.message(F.text == "Растяжка с замком за спиной")
    async def rastyazhka(message: Message):
        await message.answer("Растяжка с замком за спиной - свести согнутые руки за спиной, "
                             "стараясь коснутся пальцами двух рук. Выпрямите спину и "
                             "раскройте плечи - 15-20 секунд на каждую руку. "
                             "(Избавит вас от сутулости и улучшит гибкость спины)")
        pic = FSInputFile("upr/rastyazhka-45-350x350.jpg")
        await message.answer_photo(photo=pic)

    @staticmethod
    @router.message(F.text == "Подьем на носки и на пятки")
    async def podbem_na_noski(message: Message):
        await message.answer("Подъем на носки и на пятки - Перекат с носков на пятку - 10-12 раз "
                             "(Профилактирует варикоз и помогает избавиться от плоскостопия).")
        gif = FSInputFile("upr/Podem_na_cypochkah_perehod_na_pyatku.gif")
        await message.answer_video(video=gif)

    @staticmethod
    @router.message(F.text == "Мах ногой вперед назад")
    async def max_nogoi(message: Message):
        await message.answer("Мах ногой вперед-назад - закрепить корпус в одном положении и не наклонять "
                             "его - 10-12 раз  (Укрепляются мышцы и суставы ног, а также ягодицы, "
                             "что важно не только для эстетики, но и для нормальной работы поясницы)")
        gif = FSInputFile("upr/Mah_nogoj_vpered_nazad_razminka.gif")
        await message.answer_video(video=gif)


@router.message(F.text == "Выход")
async def exitt(message: Message):
    await message.answer("Меню", reply_markup=kb.main)


@router.message()
async def otvet(message: Message):
    await message.answer("Привет, я могу вычислить твой Индекс Массы Тела", reply_markup=kb.main)