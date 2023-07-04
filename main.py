from save import steps
from datetime import datetime as dt
from variable_constants import activities, actions, ACTIVITIES
from chart import bar_chart, circle_chart
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

keyboard = ReplyKeyboardMarkup([actions])
keyboard_choose = ReplyKeyboardMarkup([[activities[i][0] for i in activities] + ['go back']])
keyboards = [
    ReplyKeyboardMarkup([[activities[2][1][i] for i in activities[2][1]] + ['go back']]),
    ReplyKeyboardMarkup([[activities[3][1][i] for i in activities[3][1]] + ['go back']]),
    ReplyKeyboardMarkup([[activities[4][1][i] for i in activities[4][1]] + ['go back']])
]
keyboard_end = ReplyKeyboardMarkup([['end']])


async def stop(update, context):
    await update.message.reply_text('complete the program', reply_markup=ReplyKeyboardRemove())
    f = open('save.py', 'w')
    f.write('steps = [\n')
    for i in steps:
        f.write('\t' + str(i) + ',\n')
    f.write(']\n')
    f.close()
    return ConversationHandler.END


async def start(update, context):
    await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
    return 1


async def choose(update, context):
    s = 'choosing activity:\n'
    for i in range(1, len(activities) + 1):
        s += f'{activities[i][0]}\n'
    await update.message.reply_text(s, reply_markup=keyboard_choose)
    return 2


async def choosed(update, context):
    s = update.message.text
    if s == 'go back':
        await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
        return 1
    elif s == 'sleep':
        context.user_data['activities'] = s
        await update.message.reply_text(f'{s} step is underway', reply_markup=keyboard_end)
        steps.append([s, dt.now().timestamp(), ''])
        return 6
    else:
        sp = []
        for i in list(activities.values()):
            if s in i:
                sp = i
                break
        if sp:
            x, s = list(activities.keys())[list(activities.values()).index(sp)], ''
            for i in range(1, len(activities[x][1]) + 1):
                s += f'{activities[x][1][i]}\n'
            await update.message.reply_text(s, reply_markup=keyboards[x - 2])
            return x + 1
        else:
            await update.message.reply_text(f'{s} not in activities', reply_markup=keyboard_choose)
            return 2


async def relax(update, context):
    s, t = update.message.text, []
    for i in range(1, len(activities[2][1]) + 1):
        t.append(activities[2][1][i])
    if s in t:
        context.user_data['activities'] = f'relax({s})'
        await update.message.reply_text(f'relax({s}) step is underway', reply_markup=keyboard_end)
        steps.append([f'relax({s})', dt.now().timestamp(), ''])
        return 6
    elif s == 'go back':
        s = 'choosing activity:\n'
        for i in range(1, len(activities) + 1):
            s += f'{activities[i][0]}\n'
        await update.message.reply_text(s, reply_markup=keyboard_choose)
        return 2
    else:
        await update.message.reply_text(f'relax({s}) not in activities', reply_markup=keyboards[0])
        s = ''
        for i in range(1, len(activities[2][1]) + 1):
            s += f'{activities[2][1][i]}\n'
        await update.message.reply_text(s)
        return 3


async def study(update, context):
    s, t = update.message.text, []
    for i in range(1, len(activities[3][1]) + 1):
        t.append(activities[3][1][i])
    if s in t:
        context.user_data['activities'] = f'study({s})'
        await update.message.reply_text(f'study({s}) step is underway', reply_markup=keyboard_end)
        steps.append([f'study({s})', dt.now().timestamp(), ''])
        return 6
    elif s == 'go back':
        s = 'choosing activity:\n'
        for i in range(1, len(activities) + 1):
            s += f'{activities[i][0]}\n'
        await update.message.reply_text(s, reply_markup=keyboard_choose)
        return 2
    else:
        await update.message.reply_text(f'study({s}) not in activities', reply_markup=keyboards[1])
        s = ''
        for i in range(1, len(activities[3][1]) + 1):
            s += f'{activities[3][1][i]}\n'
        await update.message.reply_text(s)
        return 4


async def other(update, context):
    s, t = update.message.text, []
    for i in range(1, len(activities[4][1]) + 1):
        t.append(activities[4][1][i])
    if s in t:
        context.user_data['activities'] = f'other({s})'
        await update.message.reply_text(f'other({s}) step is underway', reply_markup=keyboard_end)
        steps.append([f'other({s})', dt.now().timestamp(), ''])
        return 6
    elif s == 'go back':
        s = 'choosing activity:\n'
        for i in range(1, len(activities) + 1):
            s += f'{activities[i][0]}\n'
        await update.message.reply_text(s, reply_markup=keyboard_choose)
        return 2
    else:
        await update.message.reply_text(f'other({s}) not in activities', reply_markup=keyboards[2])
        s = ''
        for i in range(1, len(activities[4][1]) + 1):
            s += f'{activities[4][1][i]}\n'
        await update.message.reply_text(s)
        return 5


async def end_activities(update, context):
    s = update.message.text
    if s == 'end':
        await update.message.reply_text(f'{context.user_data["activities"]} step is over', reply_markup=keyboard)
        await update.message.reply_text('\n'.join(actions))
        return 1
    await update.message.reply_text(f'please enter "end" to complete the {context.user_data["activities"]} step', reply_markup=keyboard_end)
    return 6


async def delete(update, context):
    steps.pop(-1)
    await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
    return 1


async def description(update, context):
    s = ' '.join(update.message.text.split()[1:])
    if steps:
        steps[-1][-1] = s
    await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
    return 1


async def cr_circle_chart(update, context):
    circle_chart(steps)
    await update.message.reply_photo('circle.png')
    await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
    return 1


async def cr_bar_chart(update, context):
    f = 1
    for i in steps:
        if i[0] not in ACTIVITIES:
            f = 0
            j = i[0]
    if f:
        bar_chart(steps)
        await update.message.reply_photo('bar.png')
    else:
        await update.message.reply_text(f'{j} not in ACTIVITIES')
    await update.message.reply_text('\n'.join(actions), reply_markup=keyboard)
    return 1


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CommandHandler('choosing_activity', choose), CommandHandler('create_circle_chart', cr_circle_chart),
                CommandHandler('create_bar_chart', cr_bar_chart), CommandHandler('delete_last_step', delete),
                CommandHandler('add_description_to_step', description)],
            2: [MessageHandler(filters.TEXT, choosed)],
            3: [MessageHandler(filters.TEXT, relax)],
            4: [MessageHandler(filters.TEXT, study)],
            5: [MessageHandler(filters.TEXT, other)],
            6: [MessageHandler(filters.TEXT, end_activities)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
